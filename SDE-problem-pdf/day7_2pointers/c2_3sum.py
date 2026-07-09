"""
--problem--
-----------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

--example--
-----------
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

--link--
--------
https://leetcode.com/problems/3sum/


complexity
-----------
MEDIUM

"""

class Solution:
    def threeSum(self, nums):
        
        nums = sorted(nums)
        print(nums)
        # base conditions
        length = len(nums)
        if length <= 2 :
            return []
        
        threesum_set =[]
        for a in range(0, length - 2):
            # for each we gonna run the 2 pointers (to fine the triplets)
            if a == 0 or (a > 0 and nums[a] != nums[a - 1]): # skipping the duplicates
                low = a + 1
                high = length - 1
                wanted_sum = -nums[a]
                print("low,high,wanted su",low,high,wanted_sum)
                while low < high:
                    if nums[low] + nums[high] == wanted_sum:
                        threesum_set.append([nums[a], nums[low], nums[high]])
                        print("found a triplate, skipping the duplicates")
                        # skipping the duplicates
                        while (low < high and nums[low] == nums[low + 1]): low += 1
                        while (low > high and nums[high] == nums[high + 1]): high -= 1

                        low +=1 ; high -= 1
                        print("low,high,wanted su",low,high,wanted_sum)
                    elif nums[low] + nums[high] < wanted_sum: low += 1; print("no match wanna high number than current sum sooo increasing low --> because low numbers are in left side ")
                    else: high -=1 ; print("no match wanna low number than current sum sooo decreasing high ---> high numbers are in right side")
            print("theee sum",threesum_set)
        return threesum_set

a = Solution().threeSum([-1,0,1,2,-1,-4])
print(a)
# time and space complexity
# -------------------------
# time --> O(log n) [sorting time] + O(N * N) [for each a there a linear traversal of 2 pointers low and high] 
# space -> O(m) --> triplates size

# output
"""
[-4, -1, -1, 0, 1, 2]
low,high,wanted su 1 5 4
no match wanna high number than current sum sooo increasing low --> because low numbers are in left side 
no match wanna high number than current sum sooo increasing low --> because low numbers are in left side 
no match wanna high number than current sum sooo increasing low --> because low numbers are in left side 
no match wanna high number than current sum sooo increasing low --> because low numbers are in left side 
theee sum []
low,high,wanted su 2 5 1
found a triplate, skipping the duplicates
low,high,wanted su 3 4 1
found a triplate, skipping the duplicates
low,high,wanted su 4 3 1
theee sum [[-1, -1, 2], [-1, 0, 1]]
theee sum [[-1, -1, 2], [-1, 0, 1]]
low,high,wanted su 4 5 0
no match wanna low number than current sum sooo decreasing high ---> high numbers are in right side
theee sum [[-1, -1, 2], [-1, 0, 1]]
[[-1, -1, 2], [-1, 0, 1]]
"""