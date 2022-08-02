"""
--problem--
-----------
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting
some or no elements without changing the order of the remaining elements.
--example--
-----------
Example 1:

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

--Constraints--
---------------
1 <= s.length <= 1000
s consists only of lowercase English letters.


--link--
--------
https://leetcode.com/problems/longest-palindromic-subsequence/

complexity
-----------
MEDIUM

"""


#IDEA

# if we take string and it's reversed string -- longest common subsequence is the longest polindromic substring





# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem

# time and space complexity
# -------------------------
# time --> 
# space ->


# MemoiZation(top - down) (getting dp array  in recurssion)
# ========================================================

    # step 2 :cheking the suproblem already solved or not.

    # step 3 : assign this sub problem ans to dp arrray.
# step 1 : define dp array.
# assihn one extra space and left '0' index unused-- easy to call the index.

# time and space complexity
# -------------------------
# time --> 
# space ->


# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        leN_S = len(s)
        reversed_s = ""
        for i in range(leN_S-1, -1, -1):
            reversed_s = reversed_s + s[i]
        return self.longestCommonSubsequence(s, reversed_s)

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
# time --> O(n*m) + O(n)[reversing a string]
# space -> O(n*m)


# Memory optimization (optimize space we have in tabulation)
# ==========================================================
# always initalize the second array (cur) inside the for loop -- other wise gives some error.

# time and space complexity
# -------------------------
# time --> 
# space ->




# time and space complexity
# -------------------------
# time --> 
# space ->

# output
"""

"""


