'''
Lecture 3 of IA 241
Topic: List and Set
Date: 1/31/2023
'''

#list and type showing how to print
my_list = [1,2,3,4,5] 
print(type(my_list))

#nested list is a list in a list
my_nested_list = [1,2,3,my_list]
print(my_nested_list)

#The "0" is the first item within a list
my_list[0] = 6
print(my_list)

#only prints the item within a list
print(my_list[4])

#must have the index of the desired number + 1 ":" means to split
print(my_list[:3])

#Unpack if you know how many items in a lis you can assign each item to a corresponding var
x,y,z = ['a','b','c']
print(x)
print(y)
print(z)

#append adds an item must have the "." to sperate 
my_list.append(7)
print(my_list)

#removes an item 
my_list.remove(5)
print(my_list)

#sort default is from low to high
my_list.sort()
print(my_list)

#Reverse the order in the list
my_list.reverse()
print(my_list)

#Adding a list to a list
my_list.sort()
print(my_list + [8,9])

#Extend does the same as adding a list
my_list.extend([8,9])
print(my_list)

#"In" shows the number within a list
print(2 in my_list)

#"len" shows how many items in the list
print(len(my_nested_list))