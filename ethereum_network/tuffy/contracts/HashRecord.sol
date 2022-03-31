// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HashRecord {
   // IPNS hash: SHA-256
   // Fuzzy hash: string
   mapping(uint256 => string[]) public fuzzyHashes;

   // Store fuzzy hash mapped to IPNS hash
   function setFuzzyHash(string calldata fuzzyHash, uint256 ipnsHash) public {
      fuzzyHashes[ipnsHash].push(fuzzyHash);
   }
   
   // Get fuzzy hash using IPNS hash - user should make sure matching fuzzy hash exists for the given IPNS hash
   function getFuzzyHashes(uint256 ipnsHash) public view returns (string[] memory) {
      return fuzzyHashes[ipnsHash];
   }
}
