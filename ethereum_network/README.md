# EvidenceChain

## Genesis block

- **difficulty** parameter stand for number of hash value that need to be calculated in order to find the target hash (e.g. if the difficulty is 100 and miner produces 10hashes/s then the target hash will be found in 10 seconds)
- **gasLimit** parameter stand for maximum amount of gas "burned" for a transaction 

# How to run

- Run Ethereum network

To deploy private Ethereum network using geth, have a look at launch_network.txt.

- Run IPFS client

	ipfs daemon

## Contract deployment

Run:

	truffle deploy --reset

Manual for the truffle commands: https://trufflesuite.com/docs/truffle/reference/truffle-commands/

Output:

   1_initial_migration.js
   ======================

      Replacing 'Migrations'
      ----------------------
      > transaction hash:    0x4a3243fc484a3cf7615f01c273886e2769af689675c1663625562c18612297b5
      > Blocks: 0            Seconds: 0
      > contract address:    0xab90d870C029A4bA3CfBB70A60fD0aDed5E6469B
      > block number:        1588
      > block timestamp:     1649855812
      > account:             0x79C50CF00898D316918392A8FC339E8c3348d900
      > balance:             9999999999999999999.999682706
      > gas used:            290582 (0x46f16)
      > gas price:           1 gwei
      > value sent:          0 ETH
      > total cost:          0.000290582 ETH

      > Saving migration to chain.
      > Saving artifacts
      -------------------------------------
      > Total cost:         0.000290582 ETH


   2_deploy_hash_record.js
   =======================

      Replacing 'HashRecord'
      ----------------------
      > transaction hash:    0x94eac10ee5678617d45a38def8794474ca4fb3154a52a27a8f28175ec07217d9
      > Blocks: 0            Seconds: 0
      > contract address:    0x03e69008Ee30BaB37d8A53970c06500CC77FFF26
      > block number:        1595
      > block timestamp:     1649855819
      > account:             0x79C50CF00898D316918392A8FC339E8c3348d900
      > balance:             9999999999999999999.998922636
      > gas used:            717897 (0xaf449)
      > gas price:           1 gwei
      > value sent:          0 ETH
      > total cost:          0.000717897 ETH

      > Saving migration to chain.
      > Saving artifacts
      -------------------------------------
      > Total cost:         0.000717897 ETH

   Summary
   =======
   > Total deployments:   2
   > Final cost:          0.001008479 ETH


## Interact with contract

In order to be able to use the contract, you need to find its address. 
Move to tuffy record and run bind to ethereum network:

	cd ethereum_network/tuffy
	truffle console

Inside truffle console find contracts name and its address:

	truffle(development)> HashRecord.address

Write the output of this command to **tuffy/src/call_contract.py** file (I left a comment there).

Then you run this demo file call_contract.py by:

	pipenv run python call_contract.py

This file:
a) connect to the IPFS and Ethereum Network
b) stores evidence on IPFS network and saves the returned hash
c) Stores the hash onto a Smart Contract
d) Retreives the stores hash from the Smart Contract

Expected output:

   Contract functions:  [<Function fuzzyHashes(string,uint256)>, <Function setFuzzyHash(string,string)>, <Function getFuzzyHashes(string)>, <Function deleteHashes(string)>]
   Fuzzy hash of the file: 3:kEIT/fMv:kEIT/m
   Last hash: 3:YOi0TXwSVcgLAl:YOogcl
   Chained fuzzy hash: 3:YOi0TXwSUDkh4J:YOK4qJ
   ['3:YOi0TXwSW9D81n:YOIm1n', '3:YOi0TXwSVcgLAl:YOogcl', '3:YOi0TXwSUDkh4J:YOK4qJ']
   Succesfully stored and retreived a new fuzzy hash!

I also print available function on the contract, to make it easier for you to change the code and make calls to it.
