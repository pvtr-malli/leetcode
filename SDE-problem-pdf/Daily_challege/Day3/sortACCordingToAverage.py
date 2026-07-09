# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:13:08 2021

@author: ELCOT
"""

"""
5 7 2 7 2 9 6 8
8 9 7 2
"""
def avg(a):
   
    sum_ = 0
    avg = 0
    l = len(a)
    for i in range(l):
        sum_+=a[i]
    avg = sum_ / l
    return avg
def get_min(arr,time):
    l = len(arr)
    a = arr.copy()
   
    
    for t in range(time):
        m = a[0]
        for i in range(len(a)):
            
            if a[i]<m:
                m = a[i]
        #print("The removing minimum value",m)        
        a.remove(m)
        #print("after remove",a)
                
    return m
n = int(input("Enter the number of elements in the array"))
a = list(map(int,input().split()))
k = int(input("The value of K"))
average = []
for i in range(0,n,k):
    if 
    ar = a[i: (i+k)]
    print("The sub array",ar)
    average+=[avg(ar)]
print("The averages of the array",average)
print("The array to be printed",a)
#sort pased on the avarage
l = len(average)
index=0
index_all =[]
for i in range(l):
    #print(i)
    m = get_min(average,i+1)
    #print("The minimum value",m)
    for i in range(len(average)):
        
        if average[i] == m:
            index = i
            
            index_all+=[index]
    i = k+index
    
    #print("THe average list is",index_all)
print(index_all) 
res=[]

for i in index_all:
    index=i+i
    res.extend(a[index:index+k])
print(res)        
        

    
    