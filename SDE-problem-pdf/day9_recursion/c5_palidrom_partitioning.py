"""
--problem--
-----------
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

--example--
-----------
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]

--link--
--------
https://leetcode.com/problems/palindrome-partitioning/


complexity
-----------
MEDIUM

"""


from copy import deepcopy

class Solution:
    def __init__(self) -> None:
        self.result = []

    def is_palindrom(self, string, s,e):
        sub = string[s:e+1]
        if len(sub) == 1:
            return True
        
        s,e = 0,len(sub)-1
        #print(sub,s,e)
        while not e<s:
            if sub[s] != sub[e]:
                return False
            e-=1
            s+=1
        return True

    def partition(self, s):
        def partition_rec(arr, ind, ans):
            if ind == len(arr):
                self.result.append(deepcopy(ans))
                return
            for i in range(ind, len(arr)):
                if self.is_palindrom(arr, ind,i):
                    ans.append(arr[ind:i+1])
                    partition_rec(arr, i+1, ans)
                    ans.pop() # remove the last element otherwise the first appearance of the given element will be removed -- not a correct backrancking   
        partition_rec(s, 0, [])
        return self.result

a = Solution().partition("cbbbcc")
print(a)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""