"""
--problem--
-----------
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

--example--
-----------
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

--link--
--------
https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums):
        # add all element to the dict for hasing.
        hashing_dict = {}
        long_sequence = 0
        for ele in nums:
            hashing_dict[ele] = 0
        for ele in nums:
            
            
            print("ele",ele,"count",count)
            # find the minimum value in the sequency, if it has a value lesser than this then it is not --> continue
            if ele -1  in hashing_dict:
                continue
            else:
                # check the value 
                count = 1
                while ele + 1 in hashing_dict:
                    ele += 1
                    count +=1
                print("count",count)
                if long_sequence < count:
                    long_sequence = count

            print("long seuency", long_sequence)
        return long_sequence

# a = Solution().longestConsecutive([100,4,200,1,3,2])
# print(a)

a = Solution().longestConsecutive([100,4,101,102,1,3,2])
print(a)