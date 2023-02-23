'''
Lecture 6 of IA 241
Topic: For Loop and Range function
Date: 2/21/2023
'''
'''
for loop iterates over the items of any sequence in the order that they appear 
in the sequence
'''
# for item in sequence
for num in [1,2,3]:
    print(num+1)
    print(num)

for chara in 'this is lec 6'.split():
    print(chara)
    
for num in [1,2,3]:
    if num > 1:
        print(num)
        
for word in 'this is lec6'.split():
    print(word)
    for c in word:
        print(c)

'''
Range function generates arithmetic progressions
range(m): generates progression from 0 to m-1
range(n,m): generates progression from n to m-1
range(n,m,step): generates progession from n to m-1 with an increment of the step
'''
#for i in range(5):
    #print(i)

for i in range(1,5):
    print(i)
    
#for i in range(1,5,2):
    #print(i)

'''
Breakpoint mechanism in python editor this allow for
debugging to utilize right-click on the line of code
interpreter will pause at each breakpoint this runs the code
line by line
'''

'''
Algorithm mechanical process for solving a category
of porblems, desiging algorithms is interesting, intellectually
challenging, and a central part of CS
'''
num_list = [213,321,123,312,45636,46768,465,854]
max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num
print(max_item)
