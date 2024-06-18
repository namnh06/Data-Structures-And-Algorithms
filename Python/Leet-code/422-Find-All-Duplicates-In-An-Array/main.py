# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer: List[int] = []
        
        for i in range(len(nums)):
            index: int = abs(nums[i]) - 1
            if nums[index] < 0:
                answer.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
                
        return answer
    
if __name__ == "__main__":
    s = Solution()
    
    assert s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert s.findDuplicates([1, 1, 2]) == [1]
    assert s.findDuplicates([1]) == []
    assert s.findDuplicates([2, 2, 3, 3, 4, 4]) == [2, 3, 4]
    assert s.findDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []

    print("All test cases pass")
