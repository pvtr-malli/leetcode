"""
--problem--
-----------
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

--example--
-----------
Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

--link--
--------
https://leetcode.com/problems/single-element-in-a-sorted-array/


complexity
-----------
MEDIUM

"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        Appservation:
        1. Part before single element : 1st elemts of pair is --> even index  -- 2st elemts of pair is --> odd index 
        2. Part after single element : 1st elemts of pair is --> odd index  -- 2st elemts of pair is --> even index 
        
        we are going to find the part before single ele(right side) end point.

        """
        # edge case:
        if len(nums) == 1: return nums[0]


        low = 0; high = len(nums)-2 # keeping len-2 -- edge case -- this is for single ele at the end
        print("nums",nums)
        while high >= low:
            mid = (low + high) // 2
            # are we  in correct order rigt part ?.
            if mid % 2 ==0: # even number , so next odd must same as this
                print("even mid",mid)
                if nums[mid] == nums[mid + 1]:
                    print("next odd is same moving low")
                    # we are in left part. move low
                    low = mid + 1
                else:
                    print("next odd is not same moving high")
                    high = mid -1
            else: # odd number , so before even must same as this
                print("odd mid --",mid)
                if nums[mid] == nums[mid - 1]:
                    print("before even is  same moving low")
                    # we are in left part. move low
                    low = mid + 1
                else:
                    print("before even is not same moving high")
                    high = mid -1
            print("high , low", high,low)
        return nums[low]




a = Solution().singleNonDuplicate([1,1,2])
print(a)



# time and space complexity
# -------------------------
# time -->  O(log n)
# space -> O(1)

# output
"""
nums [3, 3, 7, 7, 10, 11, 11]
odd mid -- 3
before even is  same moving low
high , low 6 4
odd mid -- 5
before even is not same moving high
high , low 4 4
even mid 4
next odd is not same moving high
high , low 3 4
10


nums [1, 1, 2]
even mid 0
next odd is same moving low
high , low 1 1
odd mid -- 1
before even is  same moving low
high , low 1 2
2

"""