# https://leetcode.com/problems/permutations/
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        answer: List[int] = []
        solution: List[int] = []

        def backtrack() -> None:
            if len(solution) == n:
                answer.append(solution[:])

            for num in nums:
                if num not in solution:
                    solution.append(num)
                    backtrack()
                    solution.pop()

        backtrack()
        return answer

if __name__ == "__main__":
    s = Solution()
    
    assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert s.permute([0,1]) == [[0,1],[1,0]]
    assert s.permute([1]) == [[1]]
