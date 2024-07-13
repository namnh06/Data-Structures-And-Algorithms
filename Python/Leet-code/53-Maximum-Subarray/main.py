# https://leetcode.com/problems/maximum-subarray/description/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        result = max_sum
        
        for i in range(1, len(nums)):
            max_sum = max(nums[i], max_sum + nums[i])
            result = max(result, max_sum)
        
        return result
    
assert Solution().maxSubArray([1, -3, 2, 1, -1]) == 3, "Test case 1 failed"
assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test case 2 failed"
assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23, "Test case 3 failed"
assert Solution().maxSubArray([-1, -2, -3, -4]) == -1, "Test case 4 failed"
assert Solution().maxSubArray([1]) == 1, "Test case 5 failed"

print("All test cases passed.")