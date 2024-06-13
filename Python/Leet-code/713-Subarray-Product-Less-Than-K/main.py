# https://leetcode.com/problems/subarray-product-less-than-k/submissions/1266932555/
# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left: int = 0
        answer: int = 0
        current = 1
        for right in range(len(nums)):
            current *= nums[right]
            while current >= k:
                current //= nums[left]
                left += 1
            
            answer += right - left + 1
        return answer

    
if __name__ == '__main__':
    s = Solution()
    
    result = s.numSubarrayProductLessThanK([1, 1, 1], 1)
    assert result == 0
    
    result = s.numSubarrayProductLessThanK([10], 100)
    assert result == 1
    
    result = s.numSubarrayProductLessThanK([10], 10)
    assert result == 0
    
    result = s.numSubarrayProductLessThanK([10, 1], 10)
    assert result == 1
    
    result = s.numSubarrayProductLessThanK([10,5,2,6], 100)
    assert result == 8
    
    result = s.numSubarrayProductLessThanK([1, 2, 3], 0)
    assert result == 0