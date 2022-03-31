// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/HashRecord.sol";

contract TestHashRecord {
   // Random SHA-256
   uint256 ipnsHash = 0xe03c6c1e303eba770681162f2e839f261cd6d4812cf95c55cbf4c5d216f768a3;

   // Random fuzzy hash
   string fuzzyHash1 = '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'; 
   string fuzzyHash2 = '3:AFHjKlVNhBGcLskrFQEv:maNhxLsr2C'; 
   string[] correctFuzzyHashes = [fuzzyHash2, fuzzyHash1];

   HashRecord hashRecord = HashRecord(DeployedAddresses.HashRecord());

   function testSetAndGetFuzzyHash() public {
   	hashRecord.setFuzzyHash(fuzzyHash2, ipnsHash);
   	hashRecord.setFuzzyHash(fuzzyHash1, ipnsHash);
   	string[] memory storedFuzzyHashes = hashRecord.getFuzzyHashes(ipnsHash);

   	Assert.equal(correctFuzzyHashes[0], storedFuzzyHashes[0], "Stored fuzzy hash 1 should match the random one");
   	Assert.equal(correctFuzzyHashes[1], storedFuzzyHashes[1], "Stored fuzzy hash 2 should match the random second one");
   }

   function deleteFuzzyHash() public {
	hashRecord.deleteHashes(ipnsHash);
   	string[] memory storedFuzzyHashes = hashRecord.getFuzzyHashes(ipnsHash);
	Assert.isEmpty(storedFuzzyHashes[0], "All the hashes for this IPNS hash should be deleted");
   }
}
