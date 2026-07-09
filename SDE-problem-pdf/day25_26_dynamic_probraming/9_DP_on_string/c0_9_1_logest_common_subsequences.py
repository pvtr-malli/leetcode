"""
--problem--
-----------
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

--example--
-----------
Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


--Constraints--
---------------
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


--link--
--------
https://leetcode.com/problems/longest-common-subsequence/


complexity
-----------
MEDIUM

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequence_rec(len(text1)-1, len(text2)-1, text1, text2)
    
    def longestCommonSubsequence_rec(self, in1, in2, text1, text2):
        if in1 < 0 or in2 < 0:
            return 0
        # if two strings match
        if text1[in1] == text2[in2]:
            return 1 + self.longestCommonSubsequence_rec(in1-1, in2-1 , text1, text2)
        # if they won't match
        else:
            # no need to put 0 below since it is not going to add any value. just putted for understanding the code flow
            return 0 + max(self.longestCommonSubsequence_rec(in1-1, in2 , text1, text2), 
                            self.longestCommonSubsequence_rec(in1, in2-1 , text1, text2))


# making the right shift of the string index. -- so that we can avoid the -ve indexing in the base while creating dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequence_rec(len(text1), len(text2), text1, text2)
    
    def longestCommonSubsequence_rec(self, in1, in2, text1, text2):
        if in1 == 0 or in2 == 0:
            return 0
        # if two strings match
        if text1[in1-1] == text2[in2-1]: # considering right shifted by 1.
            return 1 + self.longestCommonSubsequence_rec(in1-1, in2-1 , text1, text2)
        # if they won't match
        else:
            return 0 + max(self.longestCommonSubsequence_rec(in1-1, in2 , text1, text2),
                            self.longestCommonSubsequence_rec(in1, in2-1 , text1, text2))
# time and space complexity
# -------------------------
# time --> O(2**n * 2**m) (or even more -- Exponential)
# space -> O(n*m)(or even more -- Exponential)


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # step 1
        dp = []
        for i in range(n+1):
            dp.append([-1]*(m+1))
        return self.longestCommonSubsequence_rec(len(text1)-1, len(text2)-1, text1, text2, dp)
    # we can use any method above.
    def longestCommonSubsequence_rec(self, in1, in2, text1, text2, dp):
        if in1 < 0 or in2 < 0:
            return 0
        # step 3
        if dp[in1][in2] != -1:
            return dp[in1][in2]
        # if two strings match
        if text1[in1] == text2[in2]: 
            dp[in1][in2] =  1 + self.longestCommonSubsequence_rec(in1-1, in2-1 , text1, text2, dp)
        # if they won't match
        else:
            dp[in1][in2] =  max(self.longestCommonSubsequence_rec(in1-1, in2 , text1, text2, dp),
                            self.longestCommonSubsequence_rec(in1, in2-1 , text1, text2, dp))
        # step 2
        return dp[in1][in2]
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)[dp] + O(n+m)[axilory]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index.

    # ste 4: store the ans.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # step 1
        dp = []
        for i in range(n+1):
            dp.append([0]*(m+1))
        # assign the base case value

        # the below is the base case assignment , since all array values are zero no need to set it.
        # for i in range(m+1):
        #     dp[0][i] = 0
        # for j in range(n+1):
        #     dp[j][0] = 0
        # step 3
        for i in range(1, n+1):
            for j in range(1, m+1):
                # step 4
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m] 
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)[dp] 


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # step 1
        prev = [0] * (m+1)
        
        # assign the base case value

        # the below is the base case assignment , since all array values are zero no need to set it.
        # for i in range(m+1):
        #     dp[0][i] = 0
        # for j in range(n+1):
        #     dp[j][0] = 0
        # step 3
        for i in range(1, n+1):
            cur = [0] * (m+1)
            for j in range(1, m+1):
                # step 4
                if text1[i-1] == text2[j-1]:
                   cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        return prev[m] 

# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(m) * 2




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


