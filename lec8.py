'''
Lecture 8 of IA 241
Topic: Function
Date: 3/7/2023
'''
'''
Rules for taking zero or more inputs and returning a corresponding output.
Using functions makes your programs easier to write, read, test, and fix.
Define a Function
    def function_name (agruments):
'''

def cal_plus(input1, input2):
    return input1+input2
print(cal_plus(1,3))
print(cal_plus(2,7))

print("")
'''
Argument 
    An argument is a piece of information that’s passed from 
    a function call to a function
        Positional arguments: the order matters
        Keyword arguments:  name-value pairs 
Parameters
    Inside the function, the arguments are assigned to 
    variables called parameters
        You can define a default value for each parameter
        Parameters are local, and only exists inside the function
'''
def cal_plus(input1, input2):
    print(input1)
    print(input2)
    result = input1+input2
    return result
print(cal_plus(1,3))
print(cal_plus(2,7))

print("")
#Keyword Agrument
def cal_plus(input1, input2):
    print(input1)
    print(input2)
    result = input1+input2
    return result
print(cal_plus(input2=1,input1=3))
print(cal_plus(2,7))

print("")
#Parameter
def cal_plus(input1, input2=0):
    print(input1)
    print(input2)
    result = input1+input2
    return result
#print(cal_plus(input2=1,input1=3))
print(cal_plus(2))

print("")
'''
Fruitful Functions
    Functions return results are called fruitful
    functions
    
    A function can return any kind of value, 
    including lists and dictionaries.
    
    Functions don’t return results, or return None, are 
    called void functions
       As soon as a return statement runs, the function 
    terminates
'''

'''
Ex:1
    Calculating the Absolute Value
'''
def calculate_abs(a):
    if type(a) is str:
        return('Wrong data type')
    elif a>=0:
        return a
    else:
        return -a
print(calculate_abs(0))
print(calculate_abs('a'))

print("")
'''
Ex:2 
    Define a function to calculate Sigma
    Define a function to calculate Pi
'''
#Sigma
def cal_sigma(m,n):
    result = 0
    for i in range(n,m+1):
        result = result + i 
    return result
print(cal_sigma(5,2))

#Pi
def cal_pi(m,n):
    result = 1 
    for i in range(n,m+1):
        result = result * i 
    return result
print(cal_pi(5,2))

print("")
'''
Incremental Development
    Start with a working program and make small incremental changes.
    
    Use variables to hold intermediate values so you can display and check them. 
    
    Recursive Functions
        Recursive definition is the definition contains a reference to the thing being defined.
        In python, functions can call itself, i.e., recursive functions
'''

'''
Ex: 3
    Define a function to claculate a Factorial
    Define a fucntion to calculate a Permutation
'''
#Factorial 
def cal_fac(m):
    if m ==0:
        return 1
    else:
        return m*cal_fac(m-1)
print(cal_fac(0))
print(cal_fac(3))

#Permutation
def cal_p(m,n):
    return cal_fac(m)/cal_fac(m-n)
print(cal_p(5,3))