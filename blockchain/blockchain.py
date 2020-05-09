blockchain = []

""" Returun the last value of the current blockchain"""
def get_last_blockchain_value():
    return blockchain[-1]

""" Append a new value to and as well as last blockchain value to the blockchain 
Arguments:
       : transaction_amount : the amount that should be added
       :last_transaction: the last blockchain transaction(default [1])
"""
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)

def get_user_input():
    return float(input("Your tarnasaction amount please: "))

tx_amount = get_user_input()

add_value(tx_amount)
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

# Looping through the block here we would be using the two type of loo in  python to loop through the block chain
for block in blockchain:
    print('Outputting Block')
    print(block)
