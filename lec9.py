'''
Lecture 9 of IA 241
Topic: Class
Date: 3/21/2023
'''

'''
Object-Oriented Programming
    Uses programmer-defined types to organize codes and data
    Most of the computation is expressed as operations on objects.
    Objects often represent things in the real world
    Classes are essentially a template to create objects.
    Creating a new object from the defined class is called
        instantiation, and the object is an instance of the class.
'''

'''
Define a class
    class method:
        A function that is defined inside a class definition
        Is invoked on instances of that class
    class attribute:
        One of the named values associated with an object.
    class class_name:
        class_attribute = something
        def class_method(self):
            do something
'''
class car: #define a class
    maker = 'toyota' #define an attribute
    
    def report_maker(self): #define a method
        return (self.maker)
my_car = car() #create an instance
print(my_car.report_maker())

print("")

'''
__init__() Method
    When a class defines an __init__() method, class
        instantiation automatically invokes __init__() for
        the created class instance.

    class class_name:
        class_shared_attribute = something
        # class variable shared by all instances
    def __init__(self, argument):
        self. class_unique_attribute = something or argument
        # instance variable unique to each instance
'''
class car: #define a class
    maker = 'toyota' #define an attribute
#define a unique attribute
    def __init__(self,input_model):
        #assign the attribute to the input value
        self.model = input_model
    
#create instances with different attributes
my_highlander = car('highlander')
my_corolla = car('corolla')
#print the attributes
print(my_highlander.maker)
print(my_highlander.model)
print(my_corolla.maker)
print(my_corolla.model)

print("")

'''
self Argument
    The first argument of a method is called self as a
        convention.
    Methods may call other methods by using method
        attributes of the self argument
        
    class class_name:
        def __init__(self, argument):
            self. class_unique_attribute = something or argument
        def class_method(self):
            do something on self.class_unique_attribute
'''
class car: #define a class
    maker = 'toyota' #define an attribute
    #define a unique attribute
    def __init__(self,input_model):
        #assign the attribute to the input value
        self.model = input_model
    def report(self):
        #return the attribute of the instance
        return self.model, self.maker

#create an instance
my_car = car('corolla')
#call the method
print(my_car.report())

#change the attribute
my_car.maker = 'ford'
print(my_car.report())

print("")

'''
Module/ Package/Library
    A module is the py file that defines one or more functions and
        classes
    A python package refers to a directory of python module(s).
    Library:
        Designed with the aim of being usable by many applications.
        When a package is published
    import to load a python library from local machine
    pip to install a python library to the local machine
'''


import lec8
print(lec8.cal_fac(5))

import lec9
my_car = lec9.car('corolla')
print(my_car.report())