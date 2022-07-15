# Stack with max size.
class Stack:
    def __init__(self, max_size) -> None:
        self.top = -1
        self.max_size = max_size
        self.arr = [-1] * max_size
    
    def is_full(self):
        if self.top == self.max_size - 1:
            return True
        return False
    
    def is_empty(self):
        if self.top == 0:
            return True
        return False

    def peek(self):
        return self.arr[self.top]
    
    def size(self):
        return self.top + 1
    
    def push(self, val):
        if self.is_full():
            print("Stack is full")
        self.top += 1
        self.arr[self.top] = val
        

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        popped_ele = self.arr[self.top]
        self.arr[self.top] = -1 # put  a dummy value
        self.top -= 1
        return popped_ele

    def print_stack(self):
        print("="*10)
        for i in range(self.top, -1, -1):
            print(self.arr[i])
        print("="*10)

s = Stack(max_size=5)
s.push(10)
s.push(12)
s.push(13)
s.push(14)
e = s.pop()
print(e)
print("peek ele",s.peek())
print("size",s.size())
s.print_stack()
print(s.is_empty())
print(s.is_full())


# considering this as a no limit stack.
class Stack:
    def __init__(self) -> None:
        self.arr = []
    
    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return False

    def peek(self):
        return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def push(self, val):
        self.arr.append(val)
        

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        popped_ele = self.arr.pop()
        return popped_ele

    def print_stack(self):
        print("="*10)
        for i in range(len(self.arr)-1, -1, -1):
            print(self.arr[i])
        print("="*10)


s = Stack()
s.push(10)
s.push(12)
s.push(13)
s.push(14)
e = s.pop()
print(e)
print("peek ele",s.peek())
print("size",s.size())
s.print_stack()
print(s.is_empty())
