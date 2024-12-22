"""EXERCISE-1"""
import random as r
from random import randint

l1=[]
for i in range(5):
    l1.append(randint(11,99))
print(l1) #-----------------------------------------(Q1)

for i in range(3):
    num=int(input("enter 3 random number:"))
    l1.append(num)
print(l1) #-----------------------------------------(Q2)

for i in range (len(l1)):
    print(l1[i]) #----------------------------------(Q3)


""" EXERXISE-2"""
dict1={'name':'John','age':25,'address':'New york'} #-------------------(Q1)
dict1['phone']='1234567890'                         #-------------------(Q2)
print(dict1)



""" EXERCISE-3"""
set1={1,2,3,4,5} #-----------------------------------(Q1)
set1.add(6)      #-----------------------------------(Q2)
set1.remove(3)   #-----------------------------------(Q3)
print(set1)

""" EXERCISE-4"""
tuple1=(1,2,3,4)  #------------------------------------(Q1)
print(len(tuple1))#------------------------------------(Q2)
