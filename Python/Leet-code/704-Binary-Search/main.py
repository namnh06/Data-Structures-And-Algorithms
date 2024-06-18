# https://leetcode.com/problems/binary-search/submissions/1292715793/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        # Binary search
        n: int = len(nums)
        left: int = 0
        right: int = n-1

        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

s = Solution()
assert s.search([0, 1, 2, 4, 5, 6, 7], 0) == 0
assert s.search([0, 1, 2, 4, 5, 6, 7,], 3) == -1