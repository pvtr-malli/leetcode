"""
--problem--
-----------
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining
 characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

--example--
-----------
Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


--Constraints--
---------------
1 <= s.length, t.length <= 1000
s and t consist of English letters.


--link--
--------
https://leetcode.com/problems/distinct-subsequences/


complexity
-----------
HARD

"""

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.numDistinct_rec(len(s)-1, len(t)-1 , s, t)

    def numDistinct_rec(self, i,j, s1, s2):
        if j<0: return 1 
        if i<0: return 0

        # if they match
        if s1[i] == s2[j]:
            take = self.numDistinct_rec(i-1, j-1, s1,s2)
            not_take = self.numDistinct_rec(i-1, j, s1,s2)
            return take + not_take
        else:
            return self.numDistinct_rec(i-1, j ,s1,s2)


# shft index right by 1
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.numDistinct_rec(len(s), len(t), s, t)

    def numDistinct_rec(self, i,j, s1, s2):
        if j==0: return 1 
        if i==0: return 0

        # if they match
        if s1[i-1] == s2[j-1]:
            take = self.numDistinct_rec(i-1, j-1, s1,s2)
            not_take = self.numDistinct_rec(i-1, j, s1,s2)
            return take + not_take
        else:
            return self.numDistinct_rec(i-1, j ,s1,s2)

# time and space complexity
# -------------------------
# time --> O(2**n * 2**m)[exponential]
# space -> O(n+m) [exponential]


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s);m=len(t)
        dp = []
        for i in range(n+1):
            dp.append([-1]*(m+1))
        return self.numDistinct_rec(len(s)-1, len(t)-1 , s, t,dp)

    def numDistinct_rec(self, i,j, s1, s2,dp):
        if j<0: return 1 
        if i<0: return 0
        if dp[i][j] != -1 : return dp[i][j]
        # if they match
        if s1[i] == s2[j]:
            take = self.numDistinct_rec(i-1, j-1, s1,s2,dp)
            not_take = self.numDistinct_rec(i-1, j, s1,s2,dp)
            dp[i][j] = take + not_take
        else:
            dp[i][j] = self.numDistinct_rec(i-1, j ,s1,s2,dp)
        return dp[i][j]

# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n+m)[axilory] + O(n*m)[dp]


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s);m=len(t)
        dp = []
        for i in range(n+1):
            dp.append([0]*(m+1))
        
        # base case
        for i in range(0,n+1):
            dp[i][0] = 1
        # no need since already everything is zero.
        # for j in range(0,m+1):
        #     dp[0][j] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]


# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(n*m)[dp]


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s);m=len(t)
        prev = [0] * (m+1)
        
        # base case
        prev[0] = 1
        # no need since already everything is zero.
        # for j in range(0,m+1):
        #     dp[0][j] = 0
        for i in range(1, n+1):
            cur = [0] * (m+1)
            cur[0] = 1
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j-1] + prev[j]
                else:   
                    cur[j] = prev[j]
            prev = cur
        return prev[m]

# time and space complexity
# -------------------------
# time --> O(n*m)
# space -> O(m)*2

# 1D space optimizaion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s);m=len(t)
        
        # no need since already everything is zero.
        # for j in range(0,m+1):
        #     dp[0][j] = 0
        cur = [0] * (m+1)
        cur[0] = 1
        for i in range(1, n+1):
            for j in range(m, 0, -1):
                if s[i-1] == t[j-1]:
                    cur[j] = cur[j-1] + cur[j]
                # no need for this.
                # else:   
                #     cur[j] = cur[j]
        return cur[m]

# time and space complexity -- 1D
# -------------------------
# time --> O(n*m)
# space -> O(m)




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


