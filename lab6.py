''' 
IA 241 Lab 6
John Fleetwood 
Topic: for Loop and range Function
2/21/2023
'''
#3.1
for num in range(0,6):
    if num !=3:
        print(num)

#3.2
result = 1
for i in range(1,6):
    result = result * i
print(result)

#3.3
total = 0
for i in range (1,6):
    total += i
print(total)

#3.4
product = 1
for i in range(3,9):
    product *= i
print(product)

#3.5
numerator = 1 
for n in range(8,0,-1):
    numerator *= n
#print(numerator)

demoninator = 1
for d in range(3,0,-1):
    demoninator *= d
#print(demoninator)

answer = numerator / demoninator
print(answer)

#3.6
result = 0
for word in 'This is my 6th string'.split():
    result = result +1
print(result)

#3.7
my_tweet = {
            'favorite_count':1138,
            'lang':'en',
            'coordinates':(-75,40),
            'entities':{'hashtags':['Preds','Pens',"SingIntoSpring"]}
            }
hashtags_count = 0
for hashtag in my_tweet['entities']['hashtags']:
    hashtags_count += 1
print(hashtags_count)