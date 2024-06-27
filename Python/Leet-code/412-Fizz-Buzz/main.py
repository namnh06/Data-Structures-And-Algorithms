# https://leetcode.com/problems/fizz-buzz/description/

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Best Conceivable Runtime: O(n)
        
        # Brute-force Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        answer: List[str] = []
        fizz: str = "Fizz"
        buzz: str = "Buzz"
        fizzBuzz: str = fizz + buzz
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append(fizzBuzz)
            elif i % 3 == 0:
                answer.append(fizz)
            elif i % 5 == 0:
                answer.append(buzz)
            else:
                answer.append(str(i))
                
        return answer
        
s = Solution()
assert s.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], "Test case failed"
print("All test cases passed!")