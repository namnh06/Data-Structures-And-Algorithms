# https://leetcode.com/problems/find-peak-element/description/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
                
        return left
   
s = Solution() 
assert s.findPeakElement([1, 8, 3, 4, 6, 7, 8, 10]) in [1, 7]  # Peak elements could be at index 1 (8) or 7 (10)
assert s.findPeakElement([1, 2, 3, 1]) == 2  # Peak element at index 2 (value 3)
assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]  # Peaks at indices 1 (2) or 5 (6)
assert s.findPeakElement([1, 2]) == 1  # Peak element at index 1 (value 2)
assert s.findPeakElement([2, 1]) == 0  # Peak element at index 0 (value 2)
assert s.findPeakElement([1, 2, 3, 4, 5]) == 4  # Peak element at index 4 (value 5)
assert s.findPeakElement([5, 4, 3, 2, 1]) == 0  # Peak element at index 0 (value 5)
assert s.findPeakElement([1]) == 0  # Peak element at index 0 (value 1)
assert s.findPeakElement([2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) in [2, 7]  # Peaks at indices 2 (4) or 7 (3)
print("All test cases pass")
