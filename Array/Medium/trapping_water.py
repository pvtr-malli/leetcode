# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:05:57 2020

@author: ninjaac
"""


#trapping the water

class Solution:
    @staticmethod
    def water(h):
        i,j,l=0,1,len(h)-1
        result=[]
        while i!=l:
            print('i',i)
            if h[i]<h[j]:
                i+=1;j+=1
                print('ij',i,j)
            while h[i]>h[j] and j!=l:
                print('j',j)
                j+=1
                if j<i and j==l:
                    i+=1
                    j=i+1
                    print('increase ij',i,j)
            print('resukt ij',i,j)        
            result.append((min(h[i],h[j])*((j-i)-1))-sum(h[i+1:j]))
            print(result)
            i=j
            print('last i',i)
            j=i+1
        return sum(result)
print(Solution().water(h=[1,0,2,0,1,3]))