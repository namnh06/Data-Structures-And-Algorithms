from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
def test_searchInsert():
    solution = Solution()
    
    # Test case 1: Target is in the list
    nums = [1, 3, 5, 6]
    target = 5
    expected = 2
    assert solution.searchInsert(nums, target) == expected, f"Test case 1 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 2: Target is not in the list and should be inserted in the middle
    target = 2
    expected = 1
    assert solution.searchInsert(nums, target) == expected, f"Test case 2 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 3: Target is not in the list and should be inserted at the end
    target = 7
    expected = 4
    assert solution.searchInsert(nums, target) == expected, f"Test case 3 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 4: Target is not in the list and should be inserted at the beginning
    target = 0
    expected = 0
    assert solution.searchInsert(nums, target) == expected, f"Test case 4 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 5: Empty list
    nums = []
    target = 1
    expected = 0
    assert solution.searchInsert(nums, target) == expected, f"Test case 5 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 6: Single element, target is equal to element
    nums = [1]
    target = 1
    expected = 0
    assert solution.searchInsert(nums, target) == expected, f"Test case 6 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 7: Single element, target is less than element
    target = 0
    expected = 0
    assert solution.searchInsert(nums, target) == expected, f"Test case 7 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    # Test case 8: Single element, target is greater than element
    target = 2
    expected = 1
    assert solution.searchInsert(nums, target) == expected, f"Test case 8 failed: expected {expected}, got {solution.searchInsert(nums, target)}"
    
    print("All test cases passed.")

test_searchInsert()