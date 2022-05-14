# EvidenceChain

## Genesis block

The configuration for the Ethereum network is given in a so called genesis block, which for these purposes is structured as a JSON file. 
This block is the beginning or starting block of the blockchain - every peer or node connected to the Ethereum network has to know what the genesis block is so that they can do transactions - the genesis block has to be the same for every node. 
The genesis block gives a few important parameters:

- **difficulty** parameter stands for number of hash values that need to be calculated in order to find the target hash (e.g. if the difficulty is 100 and miner produces 10hashes/s then the target hash will be found in 10 seconds)
- **gasLimit** parameter stands for the maximum amount of gas "burned" for a transaction (What is gas? Namely, gas refers to the unit that measures the amount of computational effort required to execute specific operations on the Ethereum network. Since each Ethereum transaction requires computational resources to execute, each transaction requires a fee. Gas refers to the fee required to conduct a transaction on Ethereum successfully)
- **ID** of the chain can be anything, but it has to be unique. 

# How to run

Before running the network and applying configurations, a [geth account](https://geth.ethereum.org/docs/interface/managing-your-accounts) is necessary in order to be able to interact with the network.
The first step is to run the Ethereum network. To deploy a private Ethereum network using `geth`, have a look at `launch_network.txt` (you will need 3 separate terminals for this).

In short, the described configuration in our simple architecture is applied to 3 peers - the **boot node**, another node which we will call **node1**, and the **miner**. 
The boot node tells the miner where node1 is, and it tells node1 where the miner is. 
In more general terms, it tells the peers of the network how to "find" each other.

Then, run the IPFS client with `ipfs daemon` (a 4th terminal).

## Interact with contract

If this is your first time (ever) running everything, you have nothing to migrate (i.e. you cannot do anything from the next part), so you need to run the contract first. 

In order to be able to use the contract, you need to find its address. Move to tuffy record and run bind to ethereum network:

```
cd ethereum_network/tuffy
truffle console
```

Inside truffle console find contract's name and its address:

```
truffle(development)> HashRecord.address
```

Write the output of this command to `tuffy/src/call_contract.py` file (I left a comment there - it should be the `deployed_contract_address` variable). You can then run this demo file with `pipenv` (install dependencies from Pipfile by running `pipenv install` when inside `tuffy/src`):

``` 
pipenv run python call_contract.py
```

This file:
- Connects to the IPFS and Ethereum Network
- Stores evidence on IPFS network and saves the returned hash
- Stores the hash onto a Smart Contract
- Retreives the stored hash from the Smart Contract
- Optionally deletes all the hashes

Expected/example output:

      Contract functions:  [<Function fuzzyHashes(string,uint256)>, <Function setFuzzyHash(string,string)>, <Function getFuzzyHashes(string)>, <Function deleteHashes(string)>]
      Fuzzy hash of the file: 3:kEIT/fMv:kEIT/m
      Last hash: 3:YOi0TXwSVcgLAl:YOogcl
      Chained fuzzy hash: 3:YOi0TXwSUDkh4J:YOK4qJ
      ['3:YOi0TXwSW9D81n:YOIm1n', '3:YOi0TXwSVcgLAl:YOogcl', '3:YOi0TXwSUDkh4J:YOK4qJ']
      Succesfully stored and retreived a new fuzzy hash!

I also print available function on the contract, to make it easier for you to change the code and make calls to it.

## Contract deployment

Inside `ethereum_network/tuffy`, run:

```
truffle deploy --reset
```

Manual for the truffle commands: https://trufflesuite.com/docs/truffle/reference/truffle-commands/

Expected/example output:
```
   1_initial_migration.js
   ======================

      Replacing 'Migrations'
      ----------------------
      > transaction hash:    0x4a3243fc484a3cf7615f01c273886e2769af689675c1663625562c18612297b5
      > Blocks: 0            Seconds: 0 # Note: can be more than 0 seconds for some reason
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
```
This process will change the HashRecord's address, which you can obtain within `truffle console` in the same manner described above.

