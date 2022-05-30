'''
- Script currently only works for one particular evidence (and its modifications)

- Each new hash of the changed evidence is chained by prefixing it with previous fuzzy hash 

- Not only does this enable us to chronologically order the changes of the evidence but also 
extract fuzzy hashes belonging to one evidence since the chained hashes preserve similarity

Potential upgrade: add encryption to the file, before storing it on IPFS (Consequence: We then need to store ecrpytion/decryption key)
'''

import os
import sys
import json
from web3 import Web3, HTTPProvider
import ssdeep
import ipfsApi as ipfsapi
import requests

IPNS_HASH = 'k51qzi5uqu5dhxi8noqywy77j6ewm88aqbvo54b3f'

try:
    ipfs = ipfsapi.Client('127.0.0.1', 5001)
except:
    print("ERROR: Cannot connect to IPFS")
    sys.exit()

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:8545'

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Set the default account (so we don't need to set the "from" for every transaction call)
# This should be the same account address as the one unlocked during the initialization
# of the miner in ethereum_network/launch_network.txt
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = '../build/contracts/HashRecord.json'

# Deployed contract address (see `migrate` command output: `contract address`)
# NOTE: You have to change this address, since your contract address will be different
deployed_contract_address = '0x3312D8B47801037f12E7103a0A867Fb168c77388'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
# print("Contract functions: ", contract.all_functions())

# Calculate fuzzy hash of data
file_to_hash = input('Input evidence name\n')
fuzzy_hash = ssdeep.hash_from_file(file_to_hash)
print('\nFuzzy hash of the file:', fuzzy_hash)
print()

with open('last_hash.txt', 'r') as f:
    last_hash = f.read()
    print('Last hash:', last_hash)
    print()
    if last_hash != '':
        #print('Chaining hash before push to Ethereum network...')
        fuzzy_hash = ssdeep.hash(fuzzy_hash + last_hash)
        print('Chained fuzzy hash:', fuzzy_hash)
        print()

with open('last_hash.txt', 'w') as f:
    f.write(fuzzy_hash)

# Add data to IPFS
ipfs_hash = ipfs.add(file_to_hash)['Hash']

# No support from python library - therefore we call bash commands
# Adds IPFS hash to IPNS
'''
print('Adding IPFS hash to IPNS. This might take a minute...')
os.system('ipfs name publish /ipfs/' + ipfs_hash)

data_on_ipfs = os.popen("ipfs cat " + ipfs_hash).read()
#print('Data on IPFS:', data_on_ipfs)
data_on_ipns = requests.get('https://gateway.ipfs.io/ipns/' + IPNS_HASH).text
#print('Data on IPNS:', data_on_ipns)
# Sanity check
assert data_on_ipfs == data_on_ipns
'''

# Interaction with smart contract on Ethereum network
# Store hash according to IPNS hash
tx_hash = contract.functions.setFuzzyHash(fuzzy_hash, IPNS_HASH).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Retreive stored hashes according to IPNS hash
ret = contract.functions.getFuzzyHashes(IPNS_HASH).call()
print(ret)
print()

# Delete all hashes according to IPNS hash
# tx_hash = contract.functions.deleteHashes(IPNS_HASH).transact()
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print("Successfully deleted all evidence for this IPNS hash")
# print()

print('All operations successful!')
print()
