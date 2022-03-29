pragma solidity ^0.5.0;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Adoptions.sol";

contract TestAdoptions {
	Adoptions adoptions = Adoptions(DeployedAddresses.Adoptions());
	uint expectedPetId = 8;
	function testUserCanAdoptPet() public {
		uint returnedId = adoptions.adopt(expectedPetId);
		Assert.equal(returnedId, expectedPetId, "Adoption of the expected pet should match what is returned.");
	}

	address expectedAdopter = address(this);
	function testGetAdopterAddressByPetId() public {
		address adopter = adoptions.adopters(expectedPetId);
		Assert.equal(expectedAdopter, adopter, "Owner of the expected pet should be this contract");
	}
	function testGetAdopterAddressByPetIdInArray() public {
	   	address[16] memory adopters = adoptions.getAdopters();

	   	Assert.equal(adopters[expectedPetId], expectedAdopter, "Owner of the expected pet should be this contract");
	 }
}
