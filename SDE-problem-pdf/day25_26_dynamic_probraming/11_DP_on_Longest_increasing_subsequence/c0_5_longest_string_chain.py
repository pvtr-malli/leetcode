"""
--problem--
-----------
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

--example--
-----------
Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


--Constraints--
---------------
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.


--link--
--------
https://leetcode.com/problems/longest-string-chain/


complexity
-----------
MEDIUM

"""

# just getting the length

class Solution:
    def longestStrChain(self, words) -> int:
        n = len(words)
        maxi = 1
        dp = [1] * n
        words = sorted(words, key=len)
        for i in range(0,n):
            for prev_i in range(0, i):
                if self.is_posible_as_a_next_string(words[i],words[prev_i]):
                    dp[i] = max(dp[i], 1+dp[prev_i])
                maxi = max(maxi, dp[i])
        return maxi
    def is_posible_as_a_next_string(self, s1, s2):
        if not len(s1) == len(s2) +1:
            return False
        first = second = 0
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second] :
                first +=1
                second += 1
            else:
                first += 1
        # after the for loop if both present out side of the array -- return true
        if first == len(s1) and second == len(s2):
            return True
        return False

print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
# print(Solution().is_posible_as_a_next_string('ba','b'))

# to print code

class Solution:
    def longestStrChain(self, words) -> int:
        n = len(words)
        maxi = 1
        last_index = 0
        dp = [1] * n
        hash_table = [0] * n
        words = sorted(words, key=len)
        for i in range(0,n):
            hash_table[i] = i # update with default index
            for prev_i in range(0, i):
                if self.is_posible_as_a_next_string(words[i],words[prev_i]) and dp[i] < 1+dp[prev_i]:
                    dp[i] = 1+dp[prev_i]
                    hash_table[i] = prev_i
            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i

        # print it.
        ans = []
        print(hash_table)
        print(dp)
        ans.append(words[last_index])
        while last_index != hash_table[last_index]:
            last_index = hash_table[last_index]
            ans.append(words[last_index])
        print(list(reversed(ans)))  

    def is_posible_as_a_next_string(self, s1, s2):
        if not len(s1) == len(s2) +1:
            return False
        first = second = 0
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second] :
                first +=1
                second += 1
            else:
                first += 1
        # after the for loop if both present out side of the array -- return true
        if first == len(s1) and second == len(s2):
            return True
        return False
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
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



# output
"""

"""


