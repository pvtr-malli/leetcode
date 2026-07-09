"""
--problem--
-----------
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

--example--
-----------
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

--link--
--------
https://leetcode.com/problems/median-of-two-sorted-arrays/


complexity
-----------
HARD

"""

import re
import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        # always keep the first array a small one.
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        n1 = len(nums1); n2 = len(nums2)
        low = 0
        high = n1
        print("low,high", low,high)
        while low<=high:
            # we need to cut the arrays in order to find the left and right part.
            cut1 = (low + high) // 2
            cut2 = ((n1 + n2 + 1) // 2 ) - cut1 # The remaining element to get the meadin element.
            print("cut1,cut2", cut1,cut2)
            l1 = (nums1[cut1 - 1] if cut1>0 else (-sys.maxsize - 1)) # this will give the minimum integer value we have.
            l2 = (nums2[cut2 - 1] if cut2>0 else (-sys.maxsize - 1))
            print("l1,l2",l1,l2)
            r1 = (nums1[cut1] if cut1<n1 else (sys.maxsize))
            r2 = (nums2[cut2] if cut2<n2 else (sys.maxsize))
            print("r1,r2",r1,r2)
            # check the validity.
            if l1 <= r2 and l2<=r1:
                if (n1+n2) % 2 ==0:
                    return  (max(l1,l2) + min(r1,r2)) / 2
                else:
                    return max(l1,l2)
            elif(l1 > r2):
                high = cut1 -1
            else:
                low = cut1 + 1
            print("high.,low after iteration", low,high)
        return 0.0 # this is while calling the recursion function

a = Solution().findMedianSortedArrays([2], [])
print(a)




# time and space complexity
# -------------------------
# time --> O(logmin(n1,n2))
# space -> O(1)

# output
"""
low,high 0 2
cut1,cut2 1 1
l1,l2 1 3
r1,r2 2 4
high.,low after iteration 2 2
cut1,cut2 2 0
l1,l2 2 -9223372036854775808
r1,r2 9223372036854775807 3
2.5
"""