class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        # TODO: continue
        subArrays: [int] = []
        right: int = 0
        left: int = 0
        sum: int = 0
        while right < len(nums) and left < len(nums):
            if nums[right] == k and nums[right] not in subArrays:
                subArrays.append([nums[right]])
            sum += nums[right]
            while sum > k and left < right:
                sum -= nums[left]
                left += 1
            if sum == k and [nums[left],nums[right]] not in subArrays:
                subArrays.append([nums[left],nums[right]])
            left = 0
            right += 1
             
        return len(subArrays)
        
        
if __name__ == '__main__':
    s = Solution()
    # result = s.subarraySum([1], 1)
    # assert result == 1
    
    # result = s.subarraySum([2], 2)
    # assert result == 1

    # result = s.subarraySum([1, 1, 1], 2)
    # assert result == 2

    # result = s.subarraySum([1, 2, 3], 3)
    # assert result == 2
    
    result = s.subarraySum([-1, -1, 1], 0)
    assert result == 1
    
    result = s.subarraySum([1,-1,0], 0)
    assert result == 3
    
    result = s.subarraySum([1, 2, 3], 2)
    assert result == 1
    
    result = s.subarraySum([100,1,2,3,4], 6)
    assert result == 1