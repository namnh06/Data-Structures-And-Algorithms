from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest: int = nums[0]
        
        for num in nums:
            if abs(closest) > abs(num) or (abs(closest) == abs(num) and num > closest):
                closest = num
        return closest

def test_findClosestNumber():
    solution = Solution()
    assert solution.findClosestNumber([2, -1, 1]) == 1, "Test case 1 failed"
    assert solution.findClosestNumber([-4, -2, 1, 4, 8]) == 1, "Test case 2 failed"
    assert solution.findClosestNumber([3, 2, 1, -1, -2, -3]) == 1, "Test case 3 failed"
    assert solution.findClosestNumber([-3, -2, -1, 1, 2, 3]) == 1, "Test case 4 failed"
    assert solution.findClosestNumber([1, -1, 2, -2, 3, -3]) == 1, "Test case 5 failed"
    assert solution.findClosestNumber([0, 2, 3]) == 0, "Test case 6 failed"
    assert solution.findClosestNumber([-10, -5, 0, 5, 10]) == 0, "Test case 7 failed"
    assert solution.findClosestNumber([-10]) == -10, "Test case 8 failed"
    assert solution.findClosestNumber([10]) == 10, "Test case 9 failed"
    print("All test cases passed.")

test_findClosestNumber()