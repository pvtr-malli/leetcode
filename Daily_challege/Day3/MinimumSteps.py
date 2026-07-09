# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:20:28 2021

@author: ELCOT
"""

"""

find the minimum number of moves to redure n to zero

"""
def minimum(arr):
    if arr[0]<arr[1]: return arr[0]
    else: return arr[1]
def get_count(n,count):
    
    while(n>0):
    
        if(n%2==0):
            n = int(n/2)
            count+=1
            print('after reduces by second condition-->value of n',n)
        elif(n%3==0):
            n = int(n/3)
            count+=1
            print('after reduced by 3ed condition--> value of n',n)
        else:
            n -= 1
            count+=1
    return count
num = int(input("Enter the value of n--->"))
c=[]
print("THere are 2 posibilities ")
print("posibility 1")
v=get_count(num , 0)
print("The steps need to reduce N to 0 is--->",v)
c+=[v]
print("posibility 2")
n = num -1
count = 1
v = get_count(n,count)
print("The  steps need to reduce N to 0 is--->",v)
c+=[v]
print("The minimum number to reduce N to 0 is--->",minimum(c))