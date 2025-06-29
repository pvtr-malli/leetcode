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