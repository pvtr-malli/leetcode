"""
--problem--
-----------
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

--example--
-----------
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

--link--
--------
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
"""

class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_length = 0
        sum_dict = {}
        subarray_sum = 0
        for i in range(n):
            print(i)
            subarray_sum += arr[i]
            # when adding if we get zero in the middle. then that should be a longest subarray.
            if subarray_sum == 0:
                max_length =  i + 1
            else:
                # if the sum not present in dict , push it.
                if subarray_sum not in sum_dict:
                    sum_dict[subarray_sum] = i
                else:
                    max_length = max(max_length ,i - sum_dict[subarray_sum])
        # when we are completing the whole iteration and the sum is zero means the whole array sum is zero.
        if subarray_sum == 0:
            return n
        print("sum dict",sum_dict)
        print("max",max_length)
        return max_length

# a = Solution().maxLen(8, [15,-2,2,-8,1,7,10,23])
# print(a)

# a = "-341 778 -826 -153 -574 -289 -993 -622 -989 -695 150 -692 755 -150 -586 -123 960 -182 -605 168 -635 47 -108 126 158 71 -584 -482 565 -51 369 -431 431 467 305 572 -793 276 639 -706 574 158 894 -849 979 -959 432 -25 712 -897 -476 661 791 880 -686 -278 364 -123 429 -65 230 459 -770 -872 330 -202 -944 783 -502 869 -246 -154 -935 572 959 -475 18 -198 -769"
# arr = [int(ele) for ele in a.split()]
# a = Solution().maxLen(79, arr)
# print(a)

a = Solution().maxLen(4, [-1, 1, -1, 1])
print(a)

