from web3 import Web3

w3 = Web3(Web3.IPCProvider(''))
print(w3.isConnected())
