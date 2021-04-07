# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:19:14 2021

@author: ELCOT
"""
import operator
class Solution:
    def merge(self, a):
        l = len(a)
        a.sort(key = operator.itemgetter(0))
        print(a)
        res , i , re = a[0],0 , []
        while i<l :
            print('i',i)
            if res[1] > a[i+1][0]:
                res = [res[0],a[i+1][1]]
                
                print('res',res)
                
            else:
                re.append(res)
               
                print('re',re)
                res = a[i]
            i+=1        
        
        
        
Solution().merge([[1,3],[2,6],[15,18],[8,10]])        