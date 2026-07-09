"""
--problem--
-----------
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

--example--
-----------
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


--Constraints--
---------------
1 <= nums.length <= 2500
-104 <= nums[i] <= 104


--link--
--------
https://leetcode.com/problems/longest-increasing-subsequence/


complexity
-----------
MEDIUM

"""


# ALGO way



class Solution:
    def lengthOfLIS(self, nums) -> int:
        ss = []
        length = 1
        ss.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > ss[-1]:
                length+=1
                ss.append(nums[i])
            else:
                correct_ind = self.get_the_index(nums[i], ss)
                ss[correct_ind] = nums[i]
        return length

    def get_the_index(self,tar, arr):
        # get the target index -- if that is not present then the next greater ele index of target.
        # using binary search
        if len(arr) == 1: return 0
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == tar: return mid
            if arr[mid] < tar:
                low = mid+1
            else:
                high = mid-1
        return high+1

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().get_the_index(2,[1,7,8,10]))

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


