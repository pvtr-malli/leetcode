# 1 | format for monotonic stack.
- while checking always keep the stack[-1] at the left and val at the right.
```
- if increasing stack: stack[-1] > ele
- if decreasing stack: stack[-1] < ele
```
#### increasing stack.
```
for i in range(n):
while stack and arr[stack[-1]] >= arr[i]:
    next_min[stack.pop()] = i 

stack.append(i)

```

#### decreasing stack:
```
for i in range(n):

while stack and arr[stack[-1]] <= arr[i]:
    next_min[stack.pop()] = i 

stack.append(i)

```