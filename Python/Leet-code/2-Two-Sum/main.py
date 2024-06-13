# https://leetcode.com/problems/two-sum/
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

from typing import List, Dict, Tuple
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Best Conceivable Runtime: O(n)?
        
        # Brute-force solution
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
        # Hash Tables
        # Time Complexity: O(n)
        nums_map: Dict[int, int] = {}
        
        # for i, num in enumerate(nums):
        #     nums_map[num] = i
            
        # for i, num in enumerate(nums):
        #     if target - num in nums_map and i != nums_map[target - num]:
        #         return [i, nums_map[target - num]]
            
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[num] = i
            
if __name__ == "__main__":
    s = Solution()
    
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([3, 4, 9, 6, 4], 8) == [1, 4]