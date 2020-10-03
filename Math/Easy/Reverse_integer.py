# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:21:33 2020

@author: ninjaac
"""


class Solution:
    @staticmethod
    def reverse(x):
        if x==0:
            return 0
        
        result='-'

        if(x>0):
            
            result=Solution().reverse_str(x)
        else:
            
            result+=Solution().reverse_str(str(x)[1:])
        result=int(result)
        if result>0 and result>(2**31) :
            
            return 0
        if result<0 and result<(-2**31):
            return 0
        return int(result)
    
    @staticmethod
    def reverse_str(st):
        
        return (str(st))[::-1]
  

print(Solution().reverse(-2107864634))    

#the same concept from the answer 
#this may reduce the time when using the bit_length() build in function


class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0  


