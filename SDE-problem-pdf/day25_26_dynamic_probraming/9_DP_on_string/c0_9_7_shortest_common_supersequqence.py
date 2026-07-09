"""
--problem--
-----------
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

--example--
-----------
Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


--Constraints--
---------------
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.


--link--
--------
https://leetcode.com/problems/shortest-common-supersequence/


complexity
-----------
HARD

"""


# we can count the string len using recurssion and memoization.
# len(s1) - len(s2) - len(longest common subsequence)

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





# we are goin to print the string using the tabulation dp array.





# Tabulation(base/down - top) 
# ==========================
    # step 1: define the same dp size dp array.

    # step 2: assign the values of base cases.

    # step 3: Find which index to which index we need to travers and do the for loop.
    # careful about the index -- leave the base case index -- since that is already filled

        # step 4: Do what we need to do with the index. -- basically copy the recurence.

    # ste 4: store the ans.
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        return self.longestCommonSubsequence(str1, str2)
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
        

        # print the string
        ans = ""
        i = n; j = m
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                ans = text1[i-1] + ans
                i -= 1; j-= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    # move upper
                    ans = text1[i-1] + ans
                    i -= 1
                else:
                    ans = text2[j-1] + ans
                    j -= 1
        while i> 0:
            ans = text1[i-1] + ans
            i -= 1
        while j> 0:
            ans = text2[j-1] + ans
            j -= 1
        return ans
print(Solution().shortestCommonSupersequence("abac", "cab"))
# time and space complexity
# -------------------------
# time --> 
# space ->


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


