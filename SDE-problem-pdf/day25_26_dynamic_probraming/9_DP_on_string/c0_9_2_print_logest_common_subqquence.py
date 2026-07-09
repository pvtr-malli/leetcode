"""
--problem--
-----------
print any one of the longest common subsequence.


This is same as c0_9_1_logest_common_subsequences -- no recurrence code for this 
we are gonna get the string from the c0_9_1_logest_common_subsequences's tabluation dp output.
--example--
-----------



--Constraints--
---------------



--link--
--------
no


complexity
-----------


"""

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


from curses.ascii import SO


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
        #return dp[n][m] 


        # print any one longest string.
        i = len(text1)
        j = len(text2)
        lcs_str = ""
        while (i>0 and j>0):
            if text1[i-1] == text2[j-1]:
                lcs_str = text1[i-1] + lcs_str
                i = i-1
                j = j-1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i = i-1
                else:
                    j = j-1
        print(lcs_str)
Solution().longestCommonSubsequence("abcde", "ace")
 
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


