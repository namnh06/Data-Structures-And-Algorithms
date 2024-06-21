# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_search_left: bool = False) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (is_search_left and nums[mid] == target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left if is_search_left else right
        
        left = binary_search(True)
        right = binary_search()
        
        if left <= right:
            return [left,right]
        return [-1,-1]

s = Solution()

# Test cases
assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4], "Test case 1 failed"
assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1], "Test case 2 failed"
assert s.searchRange([], 0) == [-1, -1], "Test case 3 failed"
assert s.searchRange([1], 1) == [0, 0], "Test case 4 failed"
assert s.searchRange([2, 2], 2) == [0, 1], "Test case 5 failed"
assert s.searchRange([1, 2, 2, 3], 2) == [1, 2], "Test case 6 failed"
assert s.searchRange([1, 2, 3, 4, 5], 3) == [2, 2], "Test case 7 failed"
assert s.searchRange([1, 2, 3, 3, 3, 4, 5], 3) == [2, 4], "Test case 8 failed"
assert s.searchRange([1, 2, 3, 3, 3, 4, 5], 4) == [5, 5], "Test case 9 failed"
assert s.searchRange([1, 1, 1, 1, 1], 1) == [0, 4], "Test case 10 failed"
assert s.searchRange([5, 7, 7, 8, 8, 10, 10], 10) == [5, 6], "Test case 11 failed"
assert s.searchRange([5, 7, 7, 8, 8, 10, 10], 5) == [0, 0], "Test case 12 failed"
assert s.searchRange([5, 7, 7, 8, 8, 10, 10], 7) == [1, 2], "Test case 13 failed"

print("All test cases passed!")