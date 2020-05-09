Name = input('please enter your name:' )
file = open('name.txt',mode='w')
file.write(Name)
file.close()

file = open('name.txt',mode='r')
print(file.read())

# this is the session for number and variables
# variable are data container is alsorefered to as an address
age = 32
print('is {} year  old'.format(age))
# the function call int() this function converst a string to inetger
#note python has the follloeing data type Nummber (integr,float) Booolean(True,False),string which are text in quote either single or double or tripple
print(int(1.6))
address_numeb='345'
print(int(address_numeb)+3)
print(int(True))
print(int(False))
print('hello '+'world.')
amount = '34.98'
print(float(amount)+4)
# to improve the readability of float and number we could use 00000 example
# 1000000 is ame as 1_000_000 in python
1000000
fans=1_000_000
print(fans)
print(fans+3)

# working with operators (+,/,-,*) python convert division or operator to float to avoid it use // instead of /

print(3+4)
print(4-3)
print(6/3)
print(6//3)
print(5*2)
print(2**3)
print(8%5)
print('='*10)

# Advenca Number concept to point aout the number less than one problem of the computer
print(1-0.9)
#Working with string 
view = "i 'm preety a cool guy"
opinion= 'i \'m a preety cool guy'
print(view)
print(view,opinion)
long_text = """ the way the stopp is men"""
print(long_text)


