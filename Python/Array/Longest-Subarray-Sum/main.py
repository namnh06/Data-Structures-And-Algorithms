# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/
# Given an array of positive integers nums and an integer k, 
# find the length of the longest subarray whose sum is less than or equal to k. 

class Solution:
    def longest_subarray_sum(self, nums: list[int], k: int) -> int:
        left: int = 0
        answer: int = 0
        current: int = 0
        
        for right in range(len(nums)):
            current += nums[right]
            while current > k:
                current -= nums[left]
                left += 1
                
            if current == k:
                answer = max(answer, right - left + 1)
        return answer
    
if __name__ == '__main__':
    s = Solution()
    
    result = s.longest_subarray_sum([2,0,1,3,-2,1,1,1], 0)
    assert result == 3
    
    result = s.longest_subarray_sum([2,2,1,3,-2,1,1,1], 1)
    assert result == 4
    
    result = s.longest_subarray_sum([2,2,1,3], 1)
    assert result == 1
    
    result = s.longest_subarray_sum([2], 1)
    assert result == 0
    
    result = s.longest_subarray_sum([1], 1)
    assert result == 1
    
    result = s.longest_subarray_sum([1,2], 3)
    assert result == 2
    
    result = s.longest_subarray_sum([1,2,3], 3)
    assert result == 2

    result = s.longest_subarray_sum([1,2,3,1,1,1], 3)
    assert result == 3
    
    result = s.longest_subarray_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
    assert result == 4