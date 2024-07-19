from typing import List
import math
class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = [math.inf]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))
        
    def pop(self) -> int:
        self.min_stack.pop()
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
    
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3, "Test case 1 failed" # return -3
assert minStack.pop() == -3, "Test case 2 failed"
assert minStack.top() == 0, "Test case 3 failed"    # return 0
assert minStack.getMin() == -2, "Test case 4 failed" # return -2
print("All test cases passed")