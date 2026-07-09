"""
--problem--
-----------
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


--example--
-----------
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


--link--
--------
https://leetcode.com/problems/4sum/
"""

from operator import le


class Solution:
    def fourSum(self, nums, target) :
        # sort the array:
        nums = sorted(nums)
        print("sorted array",nums)
        length = len(nums)
        four_sum_list = []
        for i in range(length):
            # skip the duplicate i index
            if i >0 and nums[i] == nums[i-1]:
                continue
            print("i",i)
            for j in range(i+1, length):
                # skip the duplicate j index:
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                print("j",j)
                diff = target - (nums[i] + nums[j])
                left, right = j+1, length-1 
                print("left",left,"right",right, "diff",diff)
                while left < right:
                    two_sum = nums[left] + nums[right]
                    print("tow sum", two_sum)
                    # check the two sum equal to the needed different.
                    if two_sum == diff:
                        four_sum_list.append([nums[i], nums[j], nums[left], nums[right]])
                        # increase teh left element along with skipping the duplicate values.
                        tmp = nums[left]
                        while tmp == nums[left] and left < length-1:
                            print("inside increasing left",left)
                            left += 1
                        # increse the right pointer along with skipping the duplicate values.
                        tmp = nums[right]
                        while tmp == nums[right] and right > left:
                            print("inside increasing right")
                            right -= 1
                        
                    # when the two sum less than diff, we need to get some higher number so it make sense to move right side since the array is sorted. In this way i'll get a bigger number.
                    elif two_sum < diff:
                        # increase teh left element along with skipping the duplicate values.
                        tmp = nums[left]
                        while tmp == nums[left] and left < length-1:
                            print("inside increasing left")
                            left += 1
                    else:
                        # increse the right pointer along with skipping the duplicate values.
                        tmp = nums[right]
                        while tmp == nums[right] and right > left:
                            print("inside increasing right")
                            right -= 1
                print("left",left,"right",right, four_sum_list)
        return four_sum_list

a = Solution().fourSum([2,2,2,2,2], target=8)
print(a)                        


