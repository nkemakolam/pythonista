blockchain =[[1]]


def add_value(transaction_amount):
    blockchain.append([blockchain[-1] ,transaction_amount])
    print(blockchain)

add_value(2.4)
add_value(2.5)
add_value(1.5)
