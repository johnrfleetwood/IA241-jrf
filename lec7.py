'''
Lecture 7 of IA 241
Topic: while Loop and continue, break, and pass
Date: 2/28/2023
'''
'''
While loop
    For repeated execution aslong as it is true
While condition is true
'''

#i = 5
#while i >0:
    #i = i-1
    #print(i)
    #i = i-1

'''
Break Statment
    Breaks out of the smallest enclosing for or while loop
'''
i = 5
while i >0:
    i = i-1
    print(i)
    if i == 3:
        break
    
print("")

#nest while loop
for item in ['a', 'b']:
    print(item)
    i = 5
    while i >0:
        i = i-1
        print(i)
        if i == 3:
            break

print("")   

'''
Continue Statement
    Skips the current iteration and continue with the next 
    iteration of the loop
'''
i = 5
while i > 0:
    i=i-1
    if i == 3:
        continue
    print(i)

print("")

'''
Pass Statement
    Does Nothing
    Can be used when a statement is required syntactically BUT program
    requires no action
'''
i = 5 
while i>0:
    i=i-1
    if i==3:
        pass
    print(i)

print("")

'''
Handling Exceptions
    Errors detected during execution are exceptions
    The Try clause execute your code
    The Except clause handle error f happened in the try block
    If no exception occurs, the except clause is skipped
    If an exception occurs, the rest of the try clause is skipped. 
        The except clause is executed.
'''
try:
    print(1/0)
except ZeroDivisionError:
    print('error')

print("")

'''
In-Class Question
    Which Statement should you use to finish the while loop?
        Answer: Pass
'''
i = 5 
while i>=0:
    try:
        print(1/(i-3))
    except:
        #break
        pass
        #continue
    i=i-1