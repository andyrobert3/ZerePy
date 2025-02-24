SONIC_SWAP_ABI = [
    {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amount0In",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "_tokenIn",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "bool",
        "name": "stable",
        "type": "bool"
      }
    ],
    "name": "Swap",
    "type": "event"
  }
]

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_from", "type": "address"},
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "owner", "type": "address"},
            {"indexed": True, "name": "spender", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
]

CERC20_ABI = [{"type":"function","name":"NO_ERROR","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"_acceptAdmin","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_addReserves","inputs":[{"name":"addAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_delegateCompLikeTo","inputs":[{"name":"compLikeDelegatee","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"_reduceReserves","inputs":[{"name":"reduceAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setComptroller","inputs":[{"name":"newComptroller","type":"address","internalType":"contract ComptrollerInterface"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setInterestRateModel","inputs":[{"name":"newInterestRateModel","type":"address","internalType":"contract InterestRateModel"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setPendingAdmin","inputs":[{"name":"newPendingAdmin","type":"address","internalType":"address payable"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setProtocolSeizeShare","inputs":[{"name":"newProtocolSeizeShareMantissa","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setReserveFactor","inputs":[{"name":"newReserveFactorMantissa","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"accrualBlockTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"accrueInterest","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"admin","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address payable"}],"stateMutability":"view"},{"type":"function","name":"allowance","inputs":[{"name":"owner","type":"address","internalType":"address"},{"name":"spender","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"approve","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"balanceOf","inputs":[{"name":"owner","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"balanceOfUnderlying","inputs":[{"name":"owner","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrow","inputs":[{"name":"borrowAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrowBalanceCurrent","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrowBalanceStored","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"borrowIndex","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"borrowRatePerTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"comptroller","inputs":[],"outputs":[{"name":"","type":"address","internalType":"contract ComptrollerInterface"}],"stateMutability":"view"},{"type":"function","name":"decimals","inputs":[],"outputs":[{"name":"","type":"uint8","internalType":"uint8"}],"stateMutability":"view"},{"type":"function","name":"exchangeRateCurrent","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"exchangeRateStored","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getAccountSnapshot","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getCash","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"initialize","inputs":[{"name":"underlying_","type":"address","internalType":"address"},{"name":"comptroller_","type":"address","internalType":"contract ComptrollerInterface"},{"name":"interestRateModel_","type":"address","internalType":"contract InterestRateModel"},{"name":"initialExchangeRateMantissa_","type":"uint256","internalType":"uint256"},{"name":"name_","type":"string","internalType":"string"},{"name":"symbol_","type":"string","internalType":"string"},{"name":"decimals_","type":"uint8","internalType":"uint8"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"initialize","inputs":[{"name":"comptroller_","type":"address","internalType":"contract ComptrollerInterface"},{"name":"interestRateModel_","type":"address","internalType":"contract InterestRateModel"},{"name":"initialExchangeRateMantissa_","type":"uint256","internalType":"uint256"},{"name":"name_","type":"string","internalType":"string"},{"name":"symbol_","type":"string","internalType":"string"},{"name":"decimals_","type":"uint8","internalType":"uint8"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"interestRateModel","inputs":[],"outputs":[{"name":"","type":"address","internalType":"contract InterestRateModel"}],"stateMutability":"view"},{"type":"function","name":"isCToken","inputs":[],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"view"},{"type":"function","name":"liquidateBorrow","inputs":[{"name":"borrower","type":"address","internalType":"address"},{"name":"repayAmount","type":"uint256","internalType":"uint256"},{"name":"cTokenCollateral","type":"address","internalType":"contract CTokenInterface"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"mint","inputs":[{"name":"mintAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"mintAsCollateral","inputs":[{"name":"mintAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"name","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"pendingAdmin","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address payable"}],"stateMutability":"view"},{"type":"function","name":"protocolSeizeShareMantissa","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"redeem","inputs":[{"name":"redeemTokens","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"redeemUnderlying","inputs":[{"name":"redeemAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"repayBorrow","inputs":[{"name":"repayAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"repayBorrowBehalf","inputs":[{"name":"borrower","type":"address","internalType":"address"},{"name":"repayAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"reserveFactorMantissa","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"seize","inputs":[{"name":"liquidator","type":"address","internalType":"address"},{"name":"borrower","type":"address","internalType":"address"},{"name":"seizeTokens","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"supplyRatePerTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"sweepNative","inputs":[],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"sweepToken","inputs":[{"name":"token","type":"address","internalType":"contract EIP20NonStandardInterface"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"symbol","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"totalBorrows","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"totalBorrowsCurrent","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"totalReserves","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"totalSupply","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"transfer","inputs":[{"name":"dst","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"transferFrom","inputs":[{"name":"src","type":"address","internalType":"address"},{"name":"dst","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"underlying","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"event","name":"AccrueInterest","inputs":[{"name":"cashPrior","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"interestAccumulated","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"borrowIndex","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"totalBorrows","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Approval","inputs":[{"name":"owner","type":"address","indexed":True,"internalType":"address"},{"name":"spender","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False}]

CSONIC_ABI = [{"type":"constructor","inputs":[{"name":"comptroller_","type":"address","internalType":"contract ComptrollerInterface"},{"name":"interestRateModel_","type":"address","internalType":"contract InterestRateModel"},{"name":"initialExchangeRateMantissa_","type":"uint256","internalType":"uint256"},{"name":"name_","type":"string","internalType":"string"},{"name":"symbol_","type":"string","internalType":"string"},{"name":"decimals_","type":"uint8","internalType":"uint8"},{"name":"admin_","type":"address","internalType":"address payable"}],"stateMutability":"nonpayable"},{"type":"receive","stateMutability":"payable"},{"type":"function","name":"NO_ERROR","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"_acceptAdmin","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_addReserves","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"payable"},{"type":"function","name":"_reduceReserves","inputs":[{"name":"reduceAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setComptroller","inputs":[{"name":"newComptroller","type":"address","internalType":"contract ComptrollerInterface"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setInterestRateModel","inputs":[{"name":"newInterestRateModel","type":"address","internalType":"contract InterestRateModel"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setPendingAdmin","inputs":[{"name":"newPendingAdmin","type":"address","internalType":"address payable"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setProtocolSeizeShare","inputs":[{"name":"newProtocolSeizeShareMantissa","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"_setReserveFactor","inputs":[{"name":"newReserveFactorMantissa","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"accrualBlockTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"accrueInterest","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"admin","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address payable"}],"stateMutability":"view"},{"type":"function","name":"allowance","inputs":[{"name":"owner","type":"address","internalType":"address"},{"name":"spender","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"approve","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"balanceOf","inputs":[{"name":"owner","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"balanceOfUnderlying","inputs":[{"name":"owner","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrow","inputs":[{"name":"borrowAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrowBalanceCurrent","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"borrowBalanceStored","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"borrowIndex","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"borrowRatePerTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"comptroller","inputs":[],"outputs":[{"name":"","type":"address","internalType":"contract ComptrollerInterface"}],"stateMutability":"view"},{"type":"function","name":"decimals","inputs":[],"outputs":[{"name":"","type":"uint8","internalType":"uint8"}],"stateMutability":"view"},{"type":"function","name":"exchangeRateCurrent","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"exchangeRateStored","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getAccountSnapshot","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"},{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getCash","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"initialize","inputs":[{"name":"comptroller_","type":"address","internalType":"contract ComptrollerInterface"},{"name":"interestRateModel_","type":"address","internalType":"contract InterestRateModel"},{"name":"initialExchangeRateMantissa_","type":"uint256","internalType":"uint256"},{"name":"name_","type":"string","internalType":"string"},{"name":"symbol_","type":"string","internalType":"string"},{"name":"decimals_","type":"uint8","internalType":"uint8"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"interestRateModel","inputs":[],"outputs":[{"name":"","type":"address","internalType":"contract InterestRateModel"}],"stateMutability":"view"},{"type":"function","name":"isCToken","inputs":[],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"view"},{"type":"function","name":"liquidateBorrow","inputs":[{"name":"borrower","type":"address","internalType":"address"},{"name":"cTokenCollateral","type":"address","internalType":"contract CToken"}],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"mint","inputs":[],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"mintAsCollateral","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"payable"},{"type":"function","name":"name","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"pendingAdmin","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address payable"}],"stateMutability":"view"},{"type":"function","name":"protocolSeizeShareMantissa","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"redeem","inputs":[{"name":"redeemTokens","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"redeemUnderlying","inputs":[{"name":"redeemAmount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"repayBorrow","inputs":[],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"repayBorrowBehalf","inputs":[{"name":"borrower","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"reserveFactorMantissa","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"seize","inputs":[{"name":"liquidator","type":"address","internalType":"address"},{"name":"borrower","type":"address","internalType":"address"},{"name":"seizeTokens","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"supplyRatePerTimestamp","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"sweepToken","inputs":[{"name":"token","type":"address","internalType":"contract EIP20NonStandardInterface"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"symbol","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"totalBorrows","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"totalBorrowsCurrent","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"nonpayable"},{"type":"function","name":"totalReserves","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"totalSupply","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"transfer","inputs":[{"name":"dst","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"function","name":"transferFrom","inputs":[{"name":"src","type":"address","internalType":"address"},{"name":"dst","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"},{"type":"event","name":"AccrueInterest","inputs":[{"name":"cashPrior","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"interestAccumulated","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"borrowIndex","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"totalBorrows","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Approval","inputs":[{"name":"owner","type":"address","indexed":True,"internalType":"address"},{"name":"spender","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Borrow","inputs":[{"name":"borrower","type":"address","indexed":False,"internalType":"address"},{"name":"borrowAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"accountBorrows","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"totalBorrows","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"LiquidateBorrow","inputs":[{"name":"liquidator","type":"address","indexed":False,"internalType":"address"},{"name":"borrower","type":"address","indexed":False,"internalType":"address"},{"name":"repayAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"cTokenCollateral","type":"address","indexed":False,"internalType":"address"},{"name":"seizeTokens","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Mint","inputs":[{"name":"minter","type":"address","indexed":False,"internalType":"address"},{"name":"mintAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"mintTokens","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"NewAdmin","inputs":[{"name":"oldAdmin","type":"address","indexed":False,"internalType":"address"},{"name":"newAdmin","type":"address","indexed":False,"internalType":"address"}],"anonymous":False},{"type":"event","name":"NewComptroller","inputs":[{"name":"oldComptroller","type":"address","indexed":False,"internalType":"contract ComptrollerInterface"},{"name":"newComptroller","type":"address","indexed":False,"internalType":"contract ComptrollerInterface"}],"anonymous":False},{"type":"event","name":"NewMarketInterestRateModel","inputs":[{"name":"oldInterestRateModel","type":"address","indexed":False,"internalType":"contract InterestRateModel"},{"name":"newInterestRateModel","type":"address","indexed":False,"internalType":"contract InterestRateModel"}],"anonymous":False},{"type":"event","name":"NewPendingAdmin","inputs":[{"name":"oldPendingAdmin","type":"address","indexed":False,"internalType":"address"},{"name":"newPendingAdmin","type":"address","indexed":False,"internalType":"address"}],"anonymous":False},{"type":"event","name":"NewProtocolSeizeShare","inputs":[{"name":"oldProtocolSeizeShareMantissa","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"newProtocolSeizeShareMantissa","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"NewReserveFactor","inputs":[{"name":"oldReserveFactorMantissa","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"newReserveFactorMantissa","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Redeem","inputs":[{"name":"redeemer","type":"address","indexed":False,"internalType":"address"},{"name":"redeemAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"redeemTokens","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"RepayBorrow","inputs":[{"name":"payer","type":"address","indexed":False,"internalType":"address"},{"name":"borrower","type":"address","indexed":False,"internalType":"address"},{"name":"repayAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"accountBorrows","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"totalBorrows","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"ReservesAdded","inputs":[{"name":"benefactor","type":"address","indexed":False,"internalType":"address"},{"name":"addAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"newTotalReserves","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"ReservesReduced","inputs":[{"name":"admin","type":"address","indexed":False,"internalType":"address"},{"name":"reduceAmount","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"newTotalReserves","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Transfer","inputs":[{"name":"from","type":"address","indexed":True,"internalType":"address"},{"name":"to","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"error","name":"AcceptAdminPendingAdminCheck","inputs":[]},{"type":"error","name":"AddReservesFactorFreshCheck","inputs":[{"name":"actualAddAmount","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"BorrowCashNotAvailable","inputs":[]},{"type":"error","name":"BorrowComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"BorrowFreshnessCheck","inputs":[]},{"type":"error","name":"EnterMarketComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateAccrueBorrowInterestFailed","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateAccrueCollateralInterestFailed","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateCloseAmountIsUintMax","inputs":[]},{"type":"error","name":"LiquidateCloseAmountIsZero","inputs":[]},{"type":"error","name":"LiquidateCollateralFreshnessCheck","inputs":[]},{"type":"error","name":"LiquidateComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateFreshnessCheck","inputs":[]},{"type":"error","name":"LiquidateLiquidatorIsBorrower","inputs":[]},{"type":"error","name":"LiquidateRepayBorrowFreshFailed","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateSeizeComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"LiquidateSeizeLiquidatorIsBorrower","inputs":[]},{"type":"error","name":"MintComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"MintFreshnessCheck","inputs":[]},{"type":"error","name":"RedeemComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"RedeemFreshnessCheck","inputs":[]},{"type":"error","name":"RedeemTransferOutNotPossible","inputs":[]},{"type":"error","name":"ReduceReservesAdminCheck","inputs":[]},{"type":"error","name":"ReduceReservesCashNotAvailable","inputs":[]},{"type":"error","name":"ReduceReservesCashValidation","inputs":[]},{"type":"error","name":"ReduceReservesFreshCheck","inputs":[]},{"type":"error","name":"RepayBorrowComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"RepayBorrowFreshnessCheck","inputs":[]},{"type":"error","name":"SetComptrollerOwnerCheck","inputs":[]},{"type":"error","name":"SetInterestRateModelFreshCheck","inputs":[]},{"type":"error","name":"SetInterestRateModelOwnerCheck","inputs":[]},{"type":"error","name":"SetPendingAdminOwnerCheck","inputs":[]},{"type":"error","name":"SetProtocolSeizeShareFreshCheck","inputs":[]},{"type":"error","name":"SetProtocolSeizeShareOwnerCheck","inputs":[]},{"type":"error","name":"SetReserveFactorAdminCheck","inputs":[]},{"type":"error","name":"SetReserveFactorBoundsCheck","inputs":[]},{"type":"error","name":"SetReserveFactorFreshCheck","inputs":[]},{"type":"error","name":"TransferComptrollerRejection","inputs":[{"name":"errorCode","type":"uint256","internalType":"uint256"}]},{"type":"error","name":"TransferNotAllowed","inputs":[]},{"type":"error","name":"TransferNotEnough","inputs":[]},{"type":"error","name":"TransferTooMuch","inputs":[]}]

SILO_ABI = [
    {
        "inputs": [],
        "name": "utilizationData",
        "outputs": [
            {"internalType": "uint256", "name": "collateralAssets", "type": "uint256"},
            {"internalType": "uint256", "name": "debtAssets", "type": "uint256"},
            {"internalType": "uint256", "name": "interestRateTimestamp", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

INTEREST_RATE_MODEL_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_silo", "type": "address"},
            {"internalType": "uint256", "name": "_blockTimestamp", "type": "uint256"}
        ],
        "name": "getCurrentInterestRate",
        "outputs": [{"internalType": "uint256", "name": "rcur", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

AAVE_POOL_ABI = [
  {
        "inputs": [
            {"name": "asset", "type": "address"},
            {"name": "amount", "type": "uint256"},
            {"name": "onBehalfOf", "type": "address"},
            {"name": "referralCode", "type": "uint16"}
        ],
        "name": "supply",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"name": "asset", "type": "address"},
            {"name": "amount", "type": "uint256"},
            {"name": "to", "type": "address"}
        ],
        "name": "withdraw",
        "outputs": ["uint256"],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"name": "asset", "type": "address"}],
        "name": "getReserveData",
        "outputs": [
             {
                "internalType": "uint256",
                "name": "configurationData",
                "type": "uint256"
            },
            {
                "internalType": "uint128",
                "name": "liquidityIndex",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "currentLiquidityRate",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "variableBorrowIndex",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "currentVariableBorrowRate",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "currentStableBorrowRate",
                "type": "uint128"
            },
            {
                "internalType": "uint40",
                "name": "lastUpdateTimestamp",
                "type": "uint40"
            },
            {
                "internalType": "uint16",
                "name": "id",
                "type": "uint16"
            },
            {
                "internalType": "address",
                "name": "aTokenAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "stableDebtTokenAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "variableDebtTokenAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "interestRateStrategyAddress",
                "type": "address"
            },
            {
                "internalType": "uint128",
                "name": "accruedToTreasury",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "unbacked",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "isolationModeTotalDebt",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]