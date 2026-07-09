"""
--problem--
-----------
Given a binary array nums, return the maximum number of consecutive 1's in the array.

--example--
-----------
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

--link--
--------
https://leetcode.com/problems/max-consecutive-ones/


complexity
-----------
EASY

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        step 1: iterative over the array increase the counter when ever seeing one , otherwise make counter as zero.
        step 2: count pointer counts the consiqute ones and max pointer tracks the maximum consicutive ones.
        """
        count = 0
        maximum = 0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                count = 0
            maximum = max(count, maximum)
        return maximum




# time and space complexity
# -------------------------
# time --> O(N)
# space -> O(1)

# output
"""

"""