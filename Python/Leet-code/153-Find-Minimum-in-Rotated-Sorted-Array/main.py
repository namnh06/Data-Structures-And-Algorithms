# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        
        while left < right:
            mid: int = (left + right) // 2
            
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

if __name__ == "__main__":
    s = Solution()

    # Test case 1: Rotated at different points
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0

    # Test case 2: Not rotated (sorted array)
    assert s.findMin([1, 2, 3, 4, 5]) == 1
    assert s.findMin([2, 3, 4, 5, 6]) == 2

    # Test case 3: Single element
    assert s.findMin([1]) == 1
    assert s.findMin([10]) == 10

    # Test case 4: Two elements
    assert s.findMin([2, 1]) == 1
    assert s.findMin([1, 2]) == 1

    # Test case 5: Multiple duplicates
    assert s.findMin([2, 2, 2, 0, 1, 2]) == 0
    assert s.findMin([10, 10, 10, 5, 7, 10]) == 5

    # Test case 6: All elements same
    assert s.findMin([2, 2, 2, 2, 2]) == 2
    assert s.findMin([3, 3, 3, 3, 3]) == 3

    # Test case 7: Large rotated arrays
    assert s.findMin([6, 7, 1, 2, 3, 4, 5]) == 1
    assert s.findMin([11, 13, 15, 17, 2, 5, 8]) == 2

    # Test case 8: Rotated near start
    assert s.findMin([2, 3, 4, 5, 1]) == 1
    assert s.findMin([3, 4, 5, 1, 2]) == 1

    # Test case 9: Rotated near end
    assert s.findMin([5, 1, 2, 3, 4]) == 1
    assert s.findMin([4, 5, 1, 2, 3]) == 1

    # Test case 10: Mixed scenarios
    assert s.findMin([1, 2, 3, 4, 0]) == 0
    assert s.findMin([2, 2, 2, 3, 2, 2, 2]) == 2
    assert s.findMin([1, 2, 2, 2, 2, 2, 2, 0]) == 0
    
    print("All test cases pass")