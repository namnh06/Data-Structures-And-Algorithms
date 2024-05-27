# https://leetcode.com/problems/find-pivot-index/
# Constraints:
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n: int = len(nums)
        # Brute Force
        # for i in range (n): # Time Complexity: O(n)
        #     sumLeft: int = sum(nums[:i]) # Time Complexity: O(n^2)
        #     sumRight: int = sum(nums[i+1:]) # Time Complexity: O(n^2)
            
        #     if sumLeft == sumRight:
        #         return i
            
        # return -1
        
        # Sum Cumulative
        total: int = sum(nums)
        leftSum: int = 0
        for i in range(n): # Time Complexity: O(n)
            rightSum = total - leftSum - nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
                
        return -1
        

    
if __name__ == '__main__':
    s = Solution()
    
    result = s.pivotIndex([1, 7, 3, 6, 5, 6])
    assert result == 3
    
    result = s.pivotIndex([1, 2, 3])
    assert result == -1
    
    result = s.pivotIndex([2, 1, -1])
    assert result == 0
    
    result = s.pivotIndex([2, 1, -3, 1])
    assert result == 3