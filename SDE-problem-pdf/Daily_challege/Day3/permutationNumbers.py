# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:00:11 2021

@author: ELCOT
"""

#get the dictionary with 0-26

d= {1 : 'a' , 2:'b' , 3:'c' , 4:'d' , 5:'e' ,  6: 'f' , 7:'g' , 8:'h' , 9:'i' , 10:'j' ,11 : 'k' , 12:'l' , 13:'m' , 14:'n' , 15:'o',
    16 : 'p' , 17:'q' , 18:'r' , 19:'s' , 20:'t' ,  21: 'u' , 22:'v' , 23:'w' , 24:'x' , 25:'y' ,26 : 'z'}
n = input("Enter the number")
op = 2
seq , r = [] , []
l=len(list(n))
#joining all single element
for i in range(l):
    r+=[n[i]]
seq+=[r]
join =1
#joining the 2 values
while join<l:
    print("join",join)
    skip=join
    i = 0
    r=[]
    while i<l:
        print("INner while i",i)
        if join-1==i:
           v =n[join-1:join+1]
           i+=1
           if int(v)<26:
               r+=[v]
               print("The joined value",r)
           else:
               r=[]            
               break
        else:
            r+=[n[i]]
        i+=1
    print("The sequence",r)
    join+=1
    if (len(r)>0):
        seq+=[r]
    
#joining the 2 2 values
r=[]
for i in range(0,l,2):
    ar = n[i:i+2]
    if int(ar)<26:
        r+=[ar]
    else:
        break
seq+=[r]
print(seq)
pattern = []
for s in seq:
    c=''
    for ss in s:
        pattern+=[d[int(ss)]]
    c = "".join(pattern)
    print(c)