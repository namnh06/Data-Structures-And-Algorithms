# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # n: int = len(nums)
        # nums.sort() # Time Complexity: O(n log n)
        # if n == 1:
        #     return nums[0]
        # i: int = 1
        # while i < n: # Time Complexity: O(n)
        #     if nums[i] != nums[i-1]:
        #         return nums[i-1]
        #     i += 2
        #     if i >= n-1:
        #         return nums[n-1]
        # Space Complexity: O(1)
        
        result: int = 0
        for num in nums:
            result ^= num
        return result
        
if __name__ == '__main__':
    s = Solution()
    
    result = s.singleNumber([2,2,1])
    assert result == 1
    
    result = s.singleNumber([1,0,1])
    assert result == 0