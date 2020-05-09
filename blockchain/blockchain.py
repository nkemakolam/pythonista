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

""" Here we could stop usin the repition of user input using while loop this could make a very good 
   interface  as would be demonstrated below
   note that while true would always execute becaus etrue will always be true
"""
while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

# Looping through the block here we would be using the two type of loo in  python to loop through the block chain
    for block in blockchain:
        print('Outputting Block')
        print(block)
        
Print("Done!")