from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        result: List[int] = [1] * n
        
        prefix: int = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]
        
        suffix: int = 1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result

def test_productExceptSelf():
    solution = Solution()
    
    # Test case 1
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected, f"Test case 1 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    # Test case 2
    nums = [2, 3, 4, 5]
    expected = [60, 40, 30, 24]
    assert solution.productExceptSelf(nums) == expected, f"Test case 2 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    # Test case 3: Contains zero
    nums = [1, 0, 3, 4]
    expected = [0, 12, 0, 0]
    assert solution.productExceptSelf(nums) == expected, f"Test case 3 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    # Test case 4: All elements are zero
    nums = [0, 0, 0, 0]
    expected = [0, 0, 0, 0]
    assert solution.productExceptSelf(nums) == expected, f"Test case 4 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    # Test case 5: Single element
    nums = [1]
    expected = [1]
    assert solution.productExceptSelf(nums) == expected, f"Test case 5 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    # Test case 6: Two elements
    nums = [1, 2]
    expected = [2, 1]
    assert solution.productExceptSelf(nums) == expected, f"Test case 6 failed: expected {expected}, got {solution.productExceptSelf(nums)}"
    
    print("All test cases passed.")

test_productExceptSelf()