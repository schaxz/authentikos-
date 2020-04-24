from web3 import Web3, HTTPProvider
import binascii, contract_abi, json, pprint, subprocess, sys, time

def setup():
    '''sets up connection to solidity smart contract'''
    network = input("Enter blockchain network: ") or "Rinkeby"
    print(network)
    chain_id = get_chain_id(network)
    contract_address = input("Enter smart contract address: ") or "0xEEC42723E36b3cB362D9cB49b8Cd2a111454FF03"
    print(contract_address)
    wallet_address = input("Enter your wallet address: ") or "0xC7AC16DD7b42EeEc39Ee088a8702883e073D782e"
    print(wallet_address)
    wallet_private_key = input("Enter your private key: ") or "6065a6bd9ccc0d11fd2ffb2111e68519df26b8294489cdc45fd748dd4a4f094b"
    print(wallet_private_key)
    infura_key = input("Enter your infura api key: ") or "6c7e9aed2af146138cc7ef1986d9b558"
    print(infura_key)
    websockets_rinkeby = "wss://rinkeby.infura.io/ws/v3/" + infura_key
    ws3 = Web3(Web3.WebsocketProvider(websockets_rinkeby, websocket_kwargs={'timeout': 60}))
    https_rinkeby = "https://rinkeby.infura.io/v3/" + infura_key
    w3 = Web3(HTTPProvider(https_rinkeby))
    contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)
    return contract

def list_functions(contract):
    '''lists all smart contract functions '''
    return contract.all_functions()

# print(contract.functions.countAgencies().call())
# print(contract.functions.contractOwner().call())
# print(contract.functions.getAgencies().call())
#
# nonce = w3.eth.getTransactionCount(wallet_address)
#
# agency3 = ("ndtv.com", "0x32804f2B543f4EbEce478D9847d8446650840128")
# agency4 = ("cnbc.com", "0x6aED3Ca3C77a75Dc8d36ce9c306eA2A7aef576e0")
# setAgency(string _address, address _ethIdentity)

# txn_dict = contract.functions.setAgency(agency3[0], agency3[1]).buildTransaction({
#     'chainId': 4,
#     'gas': 140000,
#     'gasPrice': w3.toWei('40', 'gwei'),
#     'nonce': nonce,
# })

# signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = wallet_private_key)
# txn_hash_hex = (w3.eth.sendRawTransaction(signed_txn.rawTransaction)).hex()

def get_chain_id(network):
    with open('network_ids.json') as json_file: # Opening JSON file
        chains = json.load(json_file)
        chain_item = next((item for item in chains if item["name"] == network), None)
        chain_id = int(chain_item.get('chainId'), 16)
        return chain_id

if __name__ == '__main__':
    contract = setup()
    all_functions = list_functions(contract)
    print(all_functions)