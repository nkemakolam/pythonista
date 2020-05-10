""" python has the is and in boolean operator that you 
can use for some of the function  it does to compare and return true or
false transaction the folloeing example would show
""" 
# there is no switch cases in python like in other programming languages 
print(1 == 1)
print(1 is 1)
name = 'nkem'
print(name != 'chris')

data = [1,2,3]
data_test=[1,2,3]
print(data == data_test)
print(data is data_test)
print( 1 in data)
print( 5 in data_test)
print( 5 not in data)
print(data is not data_test)

# We would look at the and operator in conjuction with the with operator and the or

age = 29
if age > 20 and age < 30:
    print('between 20 and 30')

if age > 20 and age < 30 or age > 60:
    print('Yes')
# this is a sample case of grouping conditional in oython note that and takes precident before or
if name== 'chris' and (age>20 or age <30):
    print('Yes')
