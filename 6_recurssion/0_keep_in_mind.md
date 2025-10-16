- The format
```
class Solution:
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # call the recurssion call and return ans.

    def subsetsWithDup_rec(self, nums, ):
        # all the recurrsion logic goes here.

        # recurssion return logic.

        # recurssion body.
        
```


# frequently making mistakes:
- 1 | in consider all values and duplicate removal method:

I am keep on forgetting to use the ii instead of the actul ind value.
```
def combinationSum3_rec(self, cur_arr, k, target, start_ind):
    if len(cur_arr) == k:
        # we collected k elements.
        if target == 0:
            self.res.append(cur_arr.copy())
        return

    for ii in range(start_ind, 10):
        if ii <= target:
            cur_arr.append(ii)
            # self.combinationSum3_rec(cur_arr, k, target-ii, start_ind + 1).    # NOTE: Wrong have to use ii
            self.combinationSum3_rec(cur_arr, k, target-ii, ii + 1)
            cur_arr.pop()
```

- 2 | NO THINKING, if asking for without duplicate, then sort, call for loop and skip i!= ind and arr[i] == arr[i-1]
- all the duplicate sums you have to do the for loop for for ii in range(ind, n)