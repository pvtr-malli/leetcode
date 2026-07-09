"""
--problem--
-----------
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

--example--
-----------
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


--Constraints--
---------------
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.


--link--
--------
https://leetcode.com/problems/edit-distance/


complexity
-----------
HARD

"""

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         lcs = self.longestCommonSubsequence(word1, word2)
#         n = len(word1)
#         m = len(word2)
#         if n == m:
#             replace = n - lcs
#             return replace
#         if n > m:
#             delete = n - m
#             replace = m - lcs
#             return delete + replace
#         else:
#             insert = m - n
#             replace = n - lcs
#             return insert + replace



#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n = len(text1)
#         m = len(text2)
#         # step 1
#         dp = []
#         for i in range(n+1):
#             dp.append([0]*(m+1))

#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 # step 4
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         return dp[n][m] 
# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance_rec(len(word1)-1, len(word2)-1, word1, word2)

    def minDistance_rec(self, i, j , s1,s2):
        if j <0:
            return i
        if i <0:
            return j
        if s1[i] == s2[j]:
            return self.minDistance_rec(i-1,j-1, s1,s2)
        else:
            insert = 1 + self.minDistance_rec(i,j-1, s1,s2)
            delete = 1 + self.minDistance_rec(i-1,j, s1,s2)
            replace = 1 + self.minDistance_rec(i-1,j-1, s1,s2)
            return min(insert, delete, replace)

# shift index right by 1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance_rec(len(word1), len(word2), word1, word2)

    def minDistance_rec(self, i, j , s1,s2):
        if j ==0:
            return i
        if i ==0:
            return j
        if s1[i-1] == s2[j-1]:
            return self.minDistance_rec(i-1,j-1, s1,s2)
        else:
            insert = 1 + self.minDistance_rec(i,j-1, s1,s2)
            delete = 1 + self.minDistance_rec(i-1,j, s1,s2)
            replace = 1 + self.minDistance_rec(i-1,j-1, s1,s2)
            return min(insert, delete, replace)
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
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # step 1
        dp = []
        for i in range(n+1):
            dp.append([-1]*(m+1))
        return self.minDistance_rec(len(word1), len(word2), word1, word2,dp)

    def minDistance_rec(self, i, j , s1,s2,dp):
        if j ==0:
            return i
        if i ==0:
            return j
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i-1] == s2[j-1]:
            dp[i][j] =   self.minDistance_rec(i-1,j-1, s1,s2,dp)
        else:
            insert = 1 + self.minDistance_rec(i,j-1, s1,s2,dp)
            delete = 1 + self.minDistance_rec(i-1,j, s1,s2,dp)
            replace = 1 + self.minDistance_rec(i-1,j-1, s1,s2,dp)
            dp[i][j] =  min(insert, delete, replace)
        return dp[i][j]

# Success
# Details 
# Runtime: 87 ms, faster than 99.15% of Python3 online submissions for Edit Distance.
# Memory Usage: 16.8 MB, less than 81.65% of Python3 online submissions for Edit Distance.

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

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # step 1
        dp = []
        for i in range(n+1):
            dp.append([-1]*(m+1))
        for i in range(0,n+1):
            dp[i][0] = i
        for j in range (0 ,m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]
                    dp[i][j] =  min(insert, delete, replace)
        return dp[n][m]

# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)[dp] 


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # step 1
        prev = [0] * (m+1)
        for j in range (0 ,m+1):
            prev[j] = j
        for i in range(1, n+1):
            cur = [0] * (m+1)
            cur[0] = i
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    insert = 1 + cur[j-1]
                    delete = 1 + prev[j]
                    replace = 1 + prev[j-1]
                    cur[j] =  min(insert, delete, replace)
            prev = cur
        return prev[m]
# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(m)*2




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


