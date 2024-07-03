from typing import List

class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        # Time Complexity: best-case O(n); worst-case O(n)
        # Space Complexity: O(1)
        n: int = len(nums)
        for i in range(0, n, 1):
            flag: bool = False
            for j in range(0, n-i-1, 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break    
        return nums
    
assert Solution().bubble_sort([1, 2, 3]) == [1, 2, 3], "Test case 1 failed"
assert Solution().bubble_sort([3, 2, 1]) == [1, 2, 3], "Test case 2 failed"
assert Solution().bubble_sort([1, 3, 2]) == [1, 2, 3], "Test case 3 failed"
assert Solution().bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 4 failed"
assert Solution().bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 5 failed"
print("All test cases passed.")