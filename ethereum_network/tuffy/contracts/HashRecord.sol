// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HashRecord {
   // IPNS hash: string
   // Fuzzy hashes: string[]
   mapping(string => string[]) public fuzzyHashes;

   // Store fuzzy hash mapped to IPNS hash
   function setFuzzyHash(string memory fuzzyHash, string memory ipnsHash) public {
      fuzzyHashes[ipnsHash].push(fuzzyHash);
   }
   
   // Get fuzzy hash using IPNS hash - user should make sure matching fuzzy hash exists for the given IPNS hash
   function getFuzzyHashes(string memory ipnsHash) public view returns (string[] memory) {
      return fuzzyHashes[ipnsHash];
   }

   // Delete hashes stored on particular IPNS hash
   function deleteHashes(string memory ipnsHash) public {
      delete fuzzyHashes[ipnsHash];
   }
}
