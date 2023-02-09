'''
Lecture 4 of IA 241
Topic: Tuple and Dictionary
Date: 2/9/2023
'''

#this is a tuple must have a comma 
my_tuple = 'a', 'b', 'c', 'd', 'e'
print(my_tuple)
print(my_tuple[0])

#cannot edit a tuple
'''my_tuple[0] = 'f'
print(my_tuple)'''

#Dictionary (collection of Key Value pairs)
my_car = { 
         'color':'red',
         'maker':'toyota',
         'year':2015
         }
#put specific variable in the []
print(my_car['color'])
print(my_car['year'])

#Shows a list of Key Value Pairs
print(my_car.items())

#Shows a list of Keys
print(my_car.keys())

#Shows a list of the Values
print(my_car.values())

#Returns the Value of the specific Key
print(my_car.get('color'))
#Same as: print(my_car['color']

#Add a new Key Value Pair
my_car['model'] = 'venza'
print(my_car)

#Update a Key Value Pair
my_car['year'] = 2020
print(my_car)

#Len() returns the number of Key Value Pairs
print(len(my_car))

#In operator checks whether a key is in the dictionary
print('color' in my_car)

