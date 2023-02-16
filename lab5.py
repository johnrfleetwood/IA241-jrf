''' 
IA 241 Lab 5
John Fleetwood 
Topic: If Statement
2/16/2023
'''

#3.1
a_color = 'green'
if a_color == 'green':
    print('You got 5 Point')
    
#3.2
a_color = 'red'
if a_color == 'green':
    print('You got 5 Point')
else: 
    print("You got 10 points")

#3.3
favorite_fruits = ['apple', 'pear', 'blueberry']

if 'pineapple' in favorite_fruits:
    print("you really like Pineapple")
    if 'apple' in favorite_fruits:
        print('Thats my number 1 favorite too')
    if 'pear' in favorite_fruits:
        print('I also like pears')
    if 'blueberry' in favorite_fruits:
        print('I like blueberries in muffins')

#3.4
age = 21
if age < 10:
    print("this is a kid")
elif 10 <= age < 20:
    print(' This person is a teenager')
else:
    print('This person is an adult')
    if age >= 65:
        print('This person is an elder')
   

