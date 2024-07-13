from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        max_product, min_product, result = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, max_product * current, min_product * current)
            min_product = min(current, max_product * current, min_product * current)
            max_product = temp_max
            result = max(result, max_product, min_product)
            
        return result
    
solution = Solution()
assert solution.maxProduct([2, 3, -2, -4]) == 48, "Test case [2, 3, -2, -4] failed"
assert solution.maxProduct([2, 3, -2, 4]) == 6, "Test case [2, 3, -2, 4] failed"
assert solution.maxProduct([-2, 0, -1]) == 0, "Test case [-2, 0, -1] failed"
assert solution.maxProduct([2, 3, -2, 4, -1]) == 48, "Test case [2, 3, -2, 4, -1] failed"
print("All test cases passed.")