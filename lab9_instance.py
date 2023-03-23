''' 
IA 241 Lab 9 Instance
John Fleetwood 
Topic: Class
3/21/2023
'''
#3.2
from lab9_class import my_stat
my_cal = my_stat ()
print(my_cal.cal_sigma(5,3))
print(my_cal.cal_pi(5,3))
print(my_cal.cal_fac(5))
print(my_cal.cal_p(5,2))

#3.3
import numpy as np
print (np.math.factorial(999))
print(my_cal.cal_fac(999))