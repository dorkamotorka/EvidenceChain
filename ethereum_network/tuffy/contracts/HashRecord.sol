// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HashRecord {
   // IPFS hash: SHA-256
   // Fuzzy hash: string
   mapping(uint256 => string) public fuzzyHashes;

   // Store fuzzy hash mapped to ipfs hash
   function setFuzzyHash(string calldata fuzzyHash, uint256 ipfsHash) public {
	fuzzyHashes[ipfsHash] = fuzzyHash;
   }
   
   // Get fuzzy hash using IPFS hash - user should make sure matching fuzzy hash exists for the given IPFS hash
   function getFuzzyHash(uint256 ipfsHash) public view returns (string memory) {
	return fuzzyHashes[ipfsHash];
   }
}
