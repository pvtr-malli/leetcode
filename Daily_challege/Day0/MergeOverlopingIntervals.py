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
            
            if i == l-1: # insert the element in the res,when the list reaches the end
                re.append(res)
                return re
            
            elif res[1] >= a[i+1][0]:
                res = [res[0],max(res[1],a[i+1][1])]
                
                print('res',res)
            
                
            else:
                re.append(res)
               
                print('re',re)
                res = a[i+1]
                print('res updated',res)
            i+=1        
        
        
        
Solution().merge([[1,4],[2,3]])        
