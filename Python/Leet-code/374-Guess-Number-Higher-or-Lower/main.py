# https://leetcode.com/problems/guess-number-higher-or-lower/
from math import ceil
import random

class Solution:
    def guessNumber(self, n: int) -> int:
        left: int = 1
        right: int = n
        while left <= right:
            mid: int = (left + right) // 2
            result: int = guess(mid)
            
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

if __name__ == "__main__":
    n: int = 10
    picked_number: int = ceil(random.random() * n)
    def guess(num: int) -> int:
        if num == picked_number:
            return 0
        elif num > picked_number:
            return -1
        else:
            return 1
        
    assert Solution().guessNumber(n) == picked_number
    print("All test cases pass")    