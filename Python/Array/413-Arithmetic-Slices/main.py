# https://leetcode.com/problems/arithmetic-slices/description/
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

class Solution():
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n < 3:
            return 0
        # Dynamic Programming
        dp: list[int] = [0] * n # Space Complexity: O(n)
        total_slices: int = 0
        for i in range(2,n): # Time Complexity: O(n)
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                total_slices += dp[i]
                
        return total_slices
        
        # Sliding Window
        # left: int = 0
        # answer: int = 0
        # for right in range(2, n): # Time Complexity: O(n))
        #     if not nums[right] - nums[right-1] == nums[right-1] - nums[right-2]:
        #         left = right-1
        #     answer += max(right - left + 1 - 2,0)
        # # Space Complexity: O(1)
        # return answer  
    
if __name__ == "__main__":
    s = Solution()
    
    result = s.numberOfArithmeticSlices([1,2,3,8,9,10])
    assert result == 2
    result = s.numberOfArithmeticSlices([1,3,5,4,2,6,7,9])
    assert result == 1
    result = s.numberOfArithmeticSlices([1,3,5,7,9])
    assert result == 6
    result = s.numberOfArithmeticSlices([1,2,3,4,5,6])
    assert result == 10
    result = s.numberOfArithmeticSlices([1,2,3,4])
    assert result == 3
    result = s.numberOfArithmeticSlices([1,2,3])
    assert result == 1
    result = s.numberOfArithmeticSlices([1])
    assert result == 0
    
    