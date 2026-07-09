"""
--problem--
-----------
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K.
The task is to find the element that would be at the k’th position of the final sorted array.
--example--
-----------
Example 1:

Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5
Output:
6
Explanation:
The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.
Example 2:
Input:
arr1[] = {100, 112, 256, 349, 770}
arr2[] = {72, 86, 113, 119, 265, 445, 892}
k = 7
Output:
256
Explanation:
Final sorted array is - 72, 86, 100, 112,
113, 119, 256, 265, 349, 445, 770, 892
7th element of this array is 256.



You don't need to read input or print anything. Your task is to complete the function kthElement()
which takes the arrays arr1[], arr2[], its size n1 and n2 respectively and an integer K as inputs and returns the element at the Kth position.
--link--
--------

https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

complexity
-----------


"""
import sys

class Solution:
    def kthElement(self,  nums1, nums2, n1, n2, k):
        
        # always keep the first array a small one.
        if len(nums1) > len(nums2): return self.kthElement(nums2, nums1,n2,n1,k)    
        low = max(0, k-n2)
        high = min(k, n1)
        print("low,high", low,high)
        while low<=high:
            # we need to cut the arrays in order to find the left and right part.
            cut1 = (low + high) // 2
            cut2 = k - cut1 # The remaining element to get the meadin element.
            print("cut1,cut2", cut1,cut2)
            l1 = (nums1[cut1 - 1] if cut1>0 else (-sys.maxsize - 1)) # this will give the minimum integer value we have.
            l2 = (nums2[cut2 - 1] if cut2>0 else (-sys.maxsize - 1))
            print("l1,l2",l1,l2)
            r1 = (nums1[cut1] if cut1<n1 else (sys.maxsize))
            r2 = (nums2[cut2] if cut2<n2 else (sys.maxsize))
            print("r1,r2",r1,r2)
            # check the validity.
            if l1 <= r2 and l2<=r1:
                return max(l1,l2)
            elif(l1 > r2):
                high = cut1 -1
            else:
                low = cut1 + 1
            print("high.,low after iteration", low,high)
        return 0.0 # this is while calling the recursion function



# aa = "1 2 2 4 5 6 9 11 11 12 20 20 25 25 26 29 30 30 31 34 35 36 36 37 41 41 43 43 44 45 45 46 47 47 47 48 49 49 50 51 52 52 52 54 56 56 56 56 57 57 57 59 60 61 62 64 65 65 67 68 68 69 71 72 73 74 76 76 81 82 83 86 87 89 91 91 91 92 94 95 95 96 97 97 98"
# a= [int(i) for i in aa.split(" ")]
a = Solution().kthElement([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892], 5, 7, 7)
print(a)

# time and space complexity
# -------------------------
# time --> O(log min(n1,n2))
# space -> O(1)

# output
"""
input: 

a = Solution().kthElement([100, 112, 256, 349, 770],[72, 86, 113, 119, 265, 445, 892], 5, 7, 7)
print(a)


low,high 0 5
cut1,cut2 2 5
l1,l2 112 265
r1,r2 256 445
high.,low after iteration 3 5
cut1,cut2 4 3
l1,l2 349 113
r1,r2 770 119
high.,low after iteration 3 3
cut1,cut2 3 4
l1,l2 256 119
r1,r2 349 265
256



input:
aa = "1 2 2 4 5 6 9 11 11 12 20 20 25 25 26 29 30 30 31 34 35 36 36 37 41 41 43 43 44 45 45 46 47 47 47 48 49 49 50 51 52 52 52 54 56 56 56 56 57 57 57 59 60 61 62 64 65 65 67 68 68 69 71 72 73 74 76 76 81 82 83 86 87 89 91 91 91 92 94 95 95 96 97 97 98"
a= [int(i) for i in aa.split(" ")]
a = Solution().kthElement(a,[9, 53, 59, 87] , 85, 4, 19)



cut1,cut2 2 17
l1,l2 53 30
r1,r2 59 30
high.,low after iteration 0 1
cut1,cut2 0 19
l1,l2 -9223372036854775808 31
r1,r2 9 34
high.,low after iteration 1 1
cut1,cut2 1 18
l1,l2 9 30
r1,r2 53 31
30
"""