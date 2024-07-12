from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
    
    
solution = Solution()
assert solution.findMin([2, 2, 2, 0, 1]) == 0, "Test case 1 failed"
assert solution.findMin([3, 4, 5, 1, 2]) == 1, "Test case 2 failed"
assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0, "Test case 3 failed"
assert solution.findMin([11, 13, 15, 17]) == 11, "Test case 4 failed"
print("All test cases passed.")