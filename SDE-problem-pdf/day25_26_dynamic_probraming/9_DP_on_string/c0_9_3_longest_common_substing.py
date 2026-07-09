"""
--problem--
-----------
print the longest common substring


small extension of longest common subsequences

--example--
-----------



--Constraints--
---------------



--link--
--------



complexity
-----------


"""

# Recurssion
# ==========================
# step 1: represent the problem as index.-- do base case 1) destiation 2) out of bound check
# step 2: Do all stuffs with the index
# step 3: return min/max/sum --according to the problem




# my idea need dry run anc check
class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        substring_len = [0]
        self.longestCommonSubstring_rec(len(text1)-1, len(text2)-1, text1, text2, substring_len, [0])
        return substring_len[0]
    
    def longestCommonSubstring_rec(self, in1, in2, text1, text2, substring_len, longest_substring_len):
        if in1 < 0 or in2 < 0:
            return 0
        # if two strings match
        if text1[in1] == text2[in2]:
            # add one more to the substring len -- when they match.
            substring_len[0] += 1
            longest_substring_len[0] = max(longest_substring_len[0], substring_len[0])
            self.longestCommonSubstring_rec(in1-1, in2-1 , text1, text2, substring_len,longest_substring_len)
        # if they won't match
        else:
            # no need to put 0 below since it is not going to add any value. just putted for understanding the code flow
            substring_len[0] = 0
            self.longestCommonSubstring_rec(in1-1, in2 , text1, text2, substring_len,longest_substring_len), 
            self.longestCommonSubstring_rec(in1, in2-1 , text1, text2, substring_len, longest_substring_len)


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
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
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
        maxi = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                # step 4
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxi = max(maxi, dp[i][j])
                else:
                    # no need for this assignment since everything assigned to 0 in the beginning.
                    dp[i][j] = 0
        return maxi
print(Solution().longestCommonSubstring("abcde", "abcce"))
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
        maxi = 0
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
                   maxi = max(maxi, dp[i][j])
                else:
                    # no need for this assignment since everything assigned to 0 in the beginning. -- assinging here for understanding
                    cur[j] = 0
            prev = cur
        return maxi
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


