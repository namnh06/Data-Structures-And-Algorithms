# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Better Solution:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        
        # left = 0
        # right = len(nums) - 1
        
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
                
        # pivot = left
        
        # if target >= nums[pivot] and target <= nums[len(nums)-1]:
        #     left = pivot
        #     right = len(nums) - 1
        # else:
        #     left = 0
        #     right = pivot - 1
            
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
                
        # return -1
    
# Test case 1: Rotated array, target is present
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 1) == 5
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 2) == 6
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 4) == 0
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 5) == 1
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 6) == 2
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 7) == 3

# Test case 2: Rotated array, target is not present
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 8) == -1

# Test case 3: Not rotated (sorted array)
assert Solution().search([1, 2, 3, 4, 5, 6, 7], 1) == 0
assert Solution().search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert Solution().search([1, 2, 3, 4, 5, 6, 7], 7) == 6
assert Solution().search([1, 2, 3, 4, 5, 6, 7], 8) == -1

# Test case 4: Single element array
assert Solution().search([1], 1) == 0
assert Solution().search([1], 0) == -1

# Test case 5: Two element array
assert Solution().search([2, 1], 1) == 1
assert Solution().search([2, 1], 2) == 0
assert Solution().search([2, 1], 3) == -1
assert Solution().search([1, 2], 1) == 0
assert Solution().search([1, 2], 2) == 1
assert Solution().search([1, 2], 0) == -1

# Test case 6: Large rotated arrays
assert Solution().search([6, 7, 1, 2, 3, 4, 5], 1) == 2
assert Solution().search([6, 7, 1, 2, 3, 4, 5], 5) == 6
assert Solution().search([11, 13, 15, 17, 2, 5, 8], 2) == 4
assert Solution().search([11, 13, 15, 17, 2, 5, 8], 17) == 3

# Test case 8: Rotated near start
assert Solution().search([2, 3, 4, 5, 1], 1) == 4
assert Solution().search([2, 3, 4, 5, 1], 5) == 3

# Test case 9: Rotated near end
assert Solution().search([5, 1, 2, 3, 4], 1) == 1
assert Solution().search([5, 1, 2, 3, 4], 5) == 0
assert Solution().search([5, 1, 2, 3, 4], 6) == -1

# Test case 10: Mixed scenarios
assert Solution().search([1, 2, 3, 4, 0], 0) == 4
assert Solution().search([2, 2, 2, 3, 2, 2, 2], 3) == 3
assert Solution().search([1, 2, 2, 2, 2, 2, 2, 0], 0) == 7
assert Solution().search([1, 2, 2, 2, 2, 2, 2, 0], 1) == 0

print("All test cases pass")