import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:8545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
#print(web3.isConnected())
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[1]

# Path to the compiled contract JSON file
compiled_contract_path = '../build/contracts/HashRecord.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xe4c0329947178456791F04261af11E9f4369F461'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

ipfs_hash = 0xe03c6c1e303eba770681162f2e839f261cd6d4812cf95c55cbf4c5d216f768a3
fuzzy_hash = '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
tx_hash = contract.functions.setFuzzyHash(fuzzy_hash, ipfs_hash).transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
ret = contract.functions.getFuzzyHash(ipfs_hash).call()

assert ret == fuzzy_hash

print('Succesfully stored a new fuzzy hash!')

