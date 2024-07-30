from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: List[str] = []
        if len(nums) == 0:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if nums[i-1] == start:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if nums[-1] != start:
            result.append(f"{start}->{nums[-1]}")
        else:
            result.append(f"{start}")

        return result
    
def test_summaryRanges():
    solution = Solution()
    
    # Test case 1: Example provided in the problem
    nums = [0, 1, 2, 4, 5, 7]
    expected = ["0->2", "4->5", "7"]
    assert solution.summaryRanges(nums) == expected, f"Test case 1 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 2: Another example from the problem
    nums = [0, 2, 3, 4, 6, 8, 9]
    expected = ["0", "2->4", "6", "8->9"]
    assert solution.summaryRanges(nums) == expected, f"Test case 2 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 3: Single element
    nums = [1]
    expected = ["1"]
    assert solution.summaryRanges(nums) == expected, f"Test case 3 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 4: Two elements, no range
    nums = [1, 3]
    expected = ["1", "3"]
    assert solution.summaryRanges(nums) == expected, f"Test case 4 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 5: Two elements, forming a range
    nums = [1, 2]
    expected = ["1->2"]
    assert solution.summaryRanges(nums) == expected, f"Test case 5 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 6: Empty array
    nums = []
    expected = []
    assert solution.summaryRanges(nums) == expected, f"Test case 6 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 7: Larger range
    nums = [0, 1, 2, 3, 4, 5]
    expected = ["0->5"]
    assert solution.summaryRanges(nums) == expected, f"Test case 7 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 8: Negative numbers
    nums = [-3, -2, -1, 1, 2, 3]
    expected = ["-3->-1", "1->3"]
    assert solution.summaryRanges(nums) == expected, f"Test case 8 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    # Test case 9: Mixed negative and positive numbers
    nums = [-5, -4, -3, 1, 2, 5, 7, 8, 10]
    expected = ["-5->-3", "1->2", "5", "7->8", "10"]
    assert solution.summaryRanges(nums) == expected, f"Test case 9 failed: expected {expected}, got {solution.summaryRanges(nums)}"
    
    print("All test cases passed.")

test_summaryRanges()