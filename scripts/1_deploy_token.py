from brownie import TogeCoin
from scripts.helpful_scripts import get_accounts
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_accounts()
    toge_coin = TogeCoin.deploy(initial_supply, {"from": account})
    print(toge_coin.name())
