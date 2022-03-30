const HashRecord = artifacts.require("HashRecord");

module.exports = function(deployer) {
	deployer.deploy(HashRecord);
}
