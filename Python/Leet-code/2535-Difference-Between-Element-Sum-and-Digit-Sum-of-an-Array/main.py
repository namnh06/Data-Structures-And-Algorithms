# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_elements: int = sum(nums)
        sum_digits: int = 0
        
        for num in nums:
            while num > 0:
                sum_digits += num % 10
                num //= 10
                
        return abs(sum_elements - sum_digits)
    
if __name__ == "__main__":
    assert Solution().differenceOfSum([1,15,6,3]) == 9
    assert Solution().differenceOfSum([1,2,3,4]) == 0
    
    print("All test cases pass")