from typing import Dict, List

class Solution:
    def isValid(self, s: str) -> bool:
        mapping: Dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack: List[str] = []
        
        for c in s:
            if c in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[c] != top_element:
                    return False
            else:
                stack.append(c)
                
        return len(stack) == 0
    
solution = Solution()
assert solution.isValid("()") == True, "Test case 1 failed"
assert solution.isValid("()[]{}") == True, "Test case 2 failed"
assert solution.isValid("(]") == False, "Test case 3 failed"
assert solution.isValid("([)]") == False, "Test case 4 failed"
assert solution.isValid("{[]}") == True, "Test case 5 failed"
print("All test cases passed.")