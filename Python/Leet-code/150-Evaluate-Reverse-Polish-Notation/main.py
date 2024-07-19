from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        operators = {'+', '-', '*', '/'}
        stack: List[int] = []
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    result = a + b
                if c == '-':
                    result = b - a
                if c == '*':
                    result = b * a
                if c == '/':
                    result = int(b/a)
                stack.append(result)
        return stack[0]
        
solution = Solution()
assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9, "Test case 1 failed"
assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6, "Test case 2 failed"
assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, "Test case 3 failed"
print("All test cases passed.")