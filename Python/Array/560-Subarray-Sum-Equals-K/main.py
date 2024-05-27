# https://leetcode.com/problems/subarray-sum-equals-k/description/
# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        n: int  = len(nums)
        # Brute Force or Algorithm without space
        # Time Complexity: O(n^2)
        # Space Complexity: 0(1)
        # count: int = 0
        # for i in range(n):
        #     sum: int = 0
        #     for j in range(i,n):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count
        
        # Algorithm: Cumulative Sum
        # Time Complexity: O(n^2)
        # Space Complexity: 0(n)
        # if n == 1:
        #     if nums[0] == k:
        #         return 1
        #     return 0
        
        # count: int = 0
        # sum: list[int] = list(range(n + 1))
        # sum[0]: int = 0
        # for i in range(1, n + 1): # Time Complexity: 0(n)
        #     sum[i] = sum[i - 1] + nums[i - 1] # Space Complexity: 0(n)
            
        # for start in range(n + 1): # Time Complexity: 0(n)
        #     for end in range(start + 1, n + 1): # Time Complexity: 0(n^2)
        #         if (sum[end] - sum[start] == k):
        #             count += 1
        # return count
        
        # Hash map
        map: dict = {0: 1}
        count: int = 0
        sum: int = 0
        for num in nums: # Time Complexity: 0(n)
            sum += num

            if (sum - k) in map:
                count += map[sum - k]
            
            map[sum] = map.get(sum,0) + 1 # Space Complexity: 0(n)
        
        return count
        
        
if __name__ == '__main__':
    s = Solution()
    
    result = s.subarraySum([1], 1)
    assert result == 1
    
    result = s.subarraySum([2], 2)
    assert result == 1

    result = s.subarraySum([1, 1, 1], 2)
    assert result == 2

    result = s.subarraySum([1, 2, 3], 3)
    assert result == 2
    
    result = s.subarraySum([-1, -1, 1], 0)
    assert result == 1
    
    result = s.subarraySum([1,-1,0], 0)
    assert result == 3
    
    result = s.subarraySum([1, 2, 3], 2)
    assert result == 1
    
    result = s.subarraySum([100,1,2,3,4], 6)
    assert result == 1
    
    result = s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2, 7, -13, 7], 7)
    assert result == 9