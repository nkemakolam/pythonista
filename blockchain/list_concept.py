# for the block chain we use the complex data structure called list iin python denaote by []
#  list is also known as array in other programmming language
# Here we would start the basic introduction of block chaing in commmand line tom know how the tech nology workdatetime A combination of a date and a time. 
# list has a mix of value both float , integer,and string
basic_list = ['nkem', 'is', 23, """ year""", ['with lot of friend and',400.78 ,'dollar balance']]
print(basic_list)
print(len(basic_list))# the lenthg function count how long a lsit is based on the index of tge list
#to access the value stored in the list we use the name of tge list and the position of the index to reterive the value 
print(basic_list[2])
print(basic_list[4])
# here now we would use the concecpt of list to code our block chain 
# that the  block chain is made of the follwing 
""" note the the blockchain is made up of the folloeing
  the chain list or ftansaction
  1.wallet or node
  2.from who
  3.to who
  4.Transation
"""
#Steps ho the block transform and the functions in build in the python lib that makes this possible
blockchain =[1,1.6,5.1]
print(blockchain[1])
blockchain.append(4)
print(blockchain)
blockchain.pop()
print(blockchain)
