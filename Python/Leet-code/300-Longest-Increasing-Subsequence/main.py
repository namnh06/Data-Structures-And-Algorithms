from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic Programming - Binary Search
        result = list()
        for num in nums:
            left, right = 0, len(result)
            while left < right:
                mid = (left + right) // 2
                if result[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if left == len(result):
                result.append(num)
            else:
                result[left] = num
        return len(result)

solution = Solution()
assert solution.lengthOfLIS([11, 12, 13, 14, 6, 7, 8, 100]) == 5, "Test case [11, 12, 13, 14, 6, 7, 8, 100] failed"
assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Test case [10, 9, 2, 5, 3, 7, 101, 18] failed"
assert solution.lengthOfLIS([10, 9, 2, 5, 3, 4]) == 3, "Test case [10, 9, 2, 5, 3, 4] failed"
assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6, "Test case [1, 3, 6, 7, 9, 4, 10, 5, 6] failed"
assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4, "Test case [0, 1, 0, 3, 2, 3] failed"
assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1, "Test case [7, 7, 7, 7, 7, 7, 7] failed"
print("All test cases passed.")