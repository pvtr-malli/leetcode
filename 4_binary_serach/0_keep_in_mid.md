1 - Pattern for finding trues/false.

```
# [1,1,2,3,3,4,4,8,8]
# [f,f,t,t,t,t,t,t,t] -- we are looking for hte first false.

if condition meets:
    ans = mid.  # keep track of the current ans.
    # So we are looking for the first true, so go left more to see if there is anything .
    high = mid - 1
    
else:
    low = mid + 1

return ans.   # if we didn't find anything, the so far found true is the fisrt one, return it.
```


- Use cant find a min of matrix like this
```
class Solution:
    def median(self, mat):
        def count_ele(median):
            return ""
        low = min(mat)
        print(low) # will return the min whole row

```
find like this
```
low = min(row[0] for row in mat)         # smallest element (first of each row)
high = max(row[-1] for row in mat)       # largest element (last of each row)

```