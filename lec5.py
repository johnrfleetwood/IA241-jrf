'''
Lecture 5 of IA 241
Topic: Operand, Boolean, and If Statements
Date: 2/14/2023
'''

#import imports a file
import this

#can break lines
print(1+15+
            +4564)

# Id returns the 'identity of an object
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(id([1,2,3]))

#Is operator comparts the identity of the 2 object
print( a is b)

# '==' operator compares the value of the 2 objects
print(a == b)

#since it is 1 number the IDs equal
a = 1
b = 1
print(id(a))
print(id(b))
print(id(1))

print(a == b)
print(a is b)

#'None' is a datatype of its own that indicates no value
x = None
print(id(x))
print(id(None))

print(x is None)
print(x == None)
#only None can be None
a = []
print(a == None)
print(a is None)

print("")

#Boolean Types
print(True and False)
print(not False)
print(True or False)
print(not 0) #true
print(not None) #tue
print(not '0')#false string 0 is inherently true

#If Statements and Bridge Statements
if 2>1 : 
    print('2>1')
    if 3>1 :
        print('3>1')
    if 2<=1 :
        print('2<=1')
else:
    print('else statement')
print("out of 'IF' block")

print("")

#If, else statement
if 2<=1:
    print('2<=1')
else:
    print('2>1')

#elif statement
if 2>1:
    print('2>1')
elif 3>1:
    print('3>1')
else:
    print('end of elif')