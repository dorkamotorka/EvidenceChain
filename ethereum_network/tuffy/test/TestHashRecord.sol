pragma solidity >=0.4.22 <0.9.0;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/HashRecord.sol";

contract TestHashRecord {
   // Random SHA-256
   uint256 ipfsHash = 0xe03c6c1e303eba770681162f2e839f261cd6d4812cf95c55cbf4c5d216f768a3;

   // Random fuzzy hash
   string fuzzyHash = '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'; 

   HashRecord hashRecord = HashRecord(DeployedAddresses.HashRecord());

   function testSetAndGetFuzzyHash() public {
   	hashRecord.setFuzzyHash(fuzzyHash, ipfsHash);
   	string memory storedFuzzyHash = hashRecord.getFuzzyHash(ipfsHash);

   	Assert.equal(fuzzyHash, storedFuzzyHash, "Stored fuzzy hash should match the random one");
   }
}
