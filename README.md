# EvidenceChain

## Dependencies

Project uses the following tools, that you can install by:

	npm install truffle -g
	TODO

## How to run

- First run IPFS daemon

		ipfs daemon

- Then run Ethereum nodes

		geth --datadir bootnode/ --networkid 15 --nat extip:127.0.0.1

The output of this command is BOOTNODEID

	geth attach bootnode/geth.ipc --exec admin.nodeInfo.enr

- Run the rest of the network:

		geth --datadir miner --networkid 15 --port 30307 --bootnodes $BOOTNODEID --mine --miner.threads=4 --miner.etherbase=0xA36d45D2E725bcD693c47b89FF8081be2e4a39A5 --metrics --keystore ~/.ethereum/keystore --http --allow-insecure-unlock --http.addr '0.0.0.0' --http.corsdomain "*" --http.port 8545 --http.api 'personal,eth,net,web3,txpool,miner' --unlock 0x79c50cf00898d316918392a8fc339e8c3348d900

		geth --datadir node1 --networkid 15 --port 30305 --bootnodes $BOOTNODEID

- In order to interact with the smart contract on the Ethereum network run:

		cd tuffy/src
		pipenv run python call_contract.py
