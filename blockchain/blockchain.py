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

def get_transaction_value():
    user_input= float(input("Your tarnasaction amount please: "))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_element():
    
    for block in blockchain:
        print('Outputting Block')
        print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

""" Here we could stop usin the repition of user input using while loop this could make a very good 
   interface  as would be demonstrated below
   note that while true would always execute becaus etrue will always be true
"""
while True:
    print('Please make a choice: ')
    print('1: Add a new transaction value')
    print('2: I want to output the blockchain block')
    print('Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_element()
    elif user_choice == 'q':
        break
    else:
        print('you have made an ivalide selection')
       

        
print("Done!")