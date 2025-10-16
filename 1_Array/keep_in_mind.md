# Prefix Sum
- you can't calculate sufix sum in stream with O(1) time complexity, dont waste time. 


- prefix sum: for index i. the sum from (0->i) index. 
```
self.nums = nums  # [-2, 0, 3, -5, 2, -1]
prefix_sum = [self.nums[0]]
for i in range(1, len(self.nums)):
    prefix_sum.append(prefix_sum[-1] + self.nums[i])

self.ps = prefix_sum # [-2, -2, 1, -4, -2, -3]
```