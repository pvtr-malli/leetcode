# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:42:48 2020

@author: ninjaac
"""
#doing like below this the very straight forward way you can get the result but it may take a very long time
#because for each time it need to sum the even element in the list 
#it take long travese time
"""
class Solution:
    @staticmethod
    def sumEvenAfterQueries(A,queries):
        
        #defining array for storing the result
        result=[]
        
        for val,index in queries:
            
            A[index]=A[index]+val
            
            even=0
            for a in A:
                
                if(a%2==0):
                    
                    even+=a
                    
            result.append(even)
        return result


print(Solution.sumEvenAfterQueries(A=[1,2,3,4], queries=[[1,0],[-3,1],[-4,0],[2,3]]))


"""
#so reduce the above error we are going to the best way of doing this
#first sum the even values in the list as 's' every time for the below three conditions chage the value of S
# 1)even + even = even
# 2)  even + odd = evne
#  3) odd + odd = even

#for 1 -> s+= value (given)
#for 2-> s-=a value in the list
# for 3-> s= s+a+v

class Solution:
    @staticmethod
    def sumEvenAfterQueries(A,queries):
        
        #defining array for storing the result
        result=[]
        sum_even= sum( [num for num in A if num%2==0])
        for val,index in queries:
            a=A[index]
            print('a',a)
            A[index]+=val
            print(A)
            if a%2 ==0:
                if val % 2==0: sum_even+=val
                else:sum_even-=a
            else:
                if val %2!=0:sum_even+=(a+val)
            result.append(sum_even)
        return result
print(Solution.sumEvenAfterQueries(A=[1,2,3,4], queries=[[1,0],[-3,1],[-4,0],[2,3]]))

                











