'''
Lecture 2 of IA 241
Topic: Numbers Strings and Variables
Date: 1/24/2023
'''

'''Variable Types'''
print("hello") # single line comment (string variable)
print(123) # integer variable
print( type(123))
print( type('hello')) # type tells that variable it is
print( type(123.123))

'''String Methods'''
print('hello ') #single vs doulbe quotation does not matter
print("it's the second python class") # can use apostrophy in the string
print('Hello World'.upper()) #adding .upper capitizes all letters
print('     hello      world      '.strip()) #gets rid of spaces in front at back of string
print('hello word')
print('hello word'.split()) #default, split by spaces
print('hello world'.split('o')) #split by 'o'
print('hello' + " world") # + adds the str

'''Math Section'''
print(3*3) 
print(3-3)
print(3/3)
print(3+3)

'''Data Container Section'''
my_num = 123 #stores a variable
print(my_num) #calls stored var
my_num = 234
print(my_num)

