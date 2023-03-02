''' 
IA 241 Lab 7
John Fleetwood 
Topic: while Loop
3/1/2023
'''
#3.1
i = 0
while i <= 5:
    if i == 3:
        i += 1  
        continue
    print(i)
    i += 1

#3.2
i = 1
result = 1
while i <=5:
    result = result * i
    i = i +1
print(result)
    
#3.3
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total)

#3.4
product = 1
k = 3
while k <= 8:
    product *= k
    k += 1
print(product)

#3.5
numerator = 1
n = 1
while n <= 8:
    numerator *= n 
    n += 1
#print(numerator)

demoninator = 1
d = 1
while d <= 3:
    demoninator *= d
    d += 1
#print(demoninator)

answer = numerator/demoninator 
print(answer)

#3.6
num_list = [12, 32, 43, 35]
while num_list: 
    num_list.pop()  
    print(num_list)  
