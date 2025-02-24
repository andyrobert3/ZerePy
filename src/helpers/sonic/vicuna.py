from typing import Dict
from decimal import Decimal
from web3 import Web3
from web3.types import TxParams, Wei
from eth_typing import Address
from src.constants.abi import ERC20_ABI, AAVE_POOL_ABI
import logging

logger = logging.getLogger(__name__)

WRAPPED_SONIC_ADDRESS = "0x039e2fB66102314Ce7b64Ce5Ce3E5183bc94aD38"
NATIVE_TOKEN_ADDRESS = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"

class Vicuna:
    def __init__(
        self,
        web3: Web3,
        pool_addr: Address,
        whitelisted_assets: set[Address],
        account: any
    ):
        """
        Initialize Vicuna (Aave v3 fork) interface
        
        Args:
            web3: Web3 instance
            token_mapping: Mapping of token addresses to their pool addresses
            account: Account to use for transactions
        """
        self.web3 = web3
        self.account = account
        self.pool_addr = pool_addr
        self.token_mapping = whitelisted_assets

    def get_interest_rates(self, token_address: str) -> tuple[float, float]:
        """
        Get the supply and borrow interest rates for a token.
        
        Args:
            token_address: Address of token to get rates for
            
        Returns:
            Tuple of (supply_rate, borrow_rate) as normalized yearly percentages
        """
        try:
            token_address = Web3.to_checksum_address(token_address)
            if token_address not in self.token_mapping:
                raise ValueError(f"Unsupported token address: {token_address}")
            
            pool = self.web3.eth.contract(address=self.pool_addr, abi=AAVE_POOL_ABI)

            token_address = WRAPPED_SONIC_ADDRESS if token_address == NATIVE_TOKEN_ADDRESS else token_address
            
            # Get reserve data from pool
            reserve_data = pool.functions.getReserveData(token_address).call()
            
            # Convert from ray (1e27) to yearly percentage
            RAY = 1e27
            
            # Index depends on struct here https://github.com/VicunaFinance-com/Vicuna-core-bl/blob/782f51917056a53a2c228701058a6c3fb233684a/contracts/protocol/libraries/types/DataTypes.sol#L5
            current_liquidity_rate_idx = 2
            current_variable_borrow_rate_idx = 4
            supply_rate = reserve_data[current_liquidity_rate_idx] * 100 / RAY
            variable_borrow_rate = reserve_data[current_variable_borrow_rate_idx] * 100 / RAY
            
            return supply_rate, variable_borrow_rate
            
        except Exception as e:
            raise Exception(f"Failed to get interest rates for token {token_address}: {str(e)}")

    def _build_transaction_sync(self, contract_func, value: Wei = 0) -> TxParams:
        """Synchronous helper method to build a transaction with proper gas estimation"""
        gas_price = self.web3.eth.gas_price
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        
        tx_params = {
            'from': self.account.address,
            'nonce': nonce,
            'gasPrice': gas_price,
            'value': value,
        }
        
        gas_estimate = contract_func.estimate_gas(tx_params)
        tx_params['gas'] = int(gas_estimate * 1.2)  # Add 20% buffer
        
        return contract_func.build_transaction(tx_params)
