""" There are two type of loops in python 
the arr the for loop and the while loop note that the for loop is used to 
loop over an iterable like a list 
 the for loop goes ove the iterable numbers of ti e that is equalent to the lenght of the iterable
 while loop on the other hand execute on tile a certain condition
 is true see sample of the for and the while loop

 Now keep in mind the break and continue key word which is very good for quiting (break)
 or skiping an iteration in a loop then continuing the loop
"""
while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

# Looping through the block here we would be using the two type of loo in  python to loop through the block chain
    for block in blockchain:
        print('Outputting Block')
        print(block)

"""" Here we want to talk about conditional in python 