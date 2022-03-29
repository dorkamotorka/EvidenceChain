const Adoptions = artifacts.require("Adoptions");

module.exports = function(deployer) {
  deployer.deploy(Adoptions);
};
