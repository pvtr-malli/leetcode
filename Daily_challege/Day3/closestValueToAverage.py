# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:36:56 2021

@author: ELCOT
"""
"""
Find the array element which is closest to the average

i/p : 1 2 3 4 5
avg : 3 
o/p: 3 

i/p :7 12 4 18 27 37
o/p : 18
"""

n = int(input("Enter the number of elements in the array"))
a = list(map(int,input().split()))
dis = 10000000
closest_value = a[0] #initally th first value
avg ,sum_ = 0 ,0
for i in range(n):
    sum_ += a[i]
avg = int(sum_/n)

print("The avarage is",avg)

if avg in a:
    print("The closest elemnt to the Average is",avg)
else:
    for i in range(n):
        print('i',i)
        d = abs(avg - a[i])
        print('distance',d)
        if d < dis:
            dis = d
            closest_value = a[i]
    print("The closest elemnt to the Average is",closest_value)
            
        