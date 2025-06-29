# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:14:32 2021

@author: ELCOT
"""

class Solution:
    def missingNumber(self,a):
        """l = len(a)
        a_ = [i for i in range(l+1)]
        print(a_)
        a.extend(a_)
        c=a[0]
        for i in range(1,len(a)):
            print('1',c)
            print('2',a[i])
            c=c^a[i]
            print(c)"""
        
        s =sum(a)
        n=len(a)
        
        total = (n*(n+1))/2
        return int(total-s)
                
Solution().missingNumber([3,0,1])
