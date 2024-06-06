class Solution:
    def differenceK(self, nums: list[int], k: int):
        arrayLength: int = len(nums)
        if arrayLength < 2:
            return 0
        result: int = 0
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # for i in range(arrayLength):
        #     for j in range(i+1, arrayLength):
        #         if abs(nums[i] - nums[j]) == k:
        #             result += 1
        # return result
        
        # Sorted with Binary Search
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        nums.sort()
        def binary_search(nums, start, target):
            left, right = start, len(nums) - 1
            while left <= right:
                mid: int = left + (right-left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for i in range(arrayLength):
            target: int = nums[i] + k
            j: int = binary_search(nums, i+1, target) # O(log n)
            if not j == -1:
                result += 1
                    
        return result
        
        # Hash Tables
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # nums_set = set(nums)
        # for num in nums:
        #     if num + k in nums_set:
        #         result += 1
                
        # return result
    
if __name__ == "__main__":
    s = Solution()
    
    # assert s.differenceK([], 2) == 0
    # assert s.differenceK([1], 2) == 0
    assert s.differenceK([1, 7, 5, 9, 2, 12, 3], 2) == 4
    assert s.differenceK([1, -2, 5, 9, 2, 12, 3], 4) == 3
    assert s.differenceK([1, 3, 5, 4], 2) == 2
    assert s.differenceK([1, 2, 3, 4], 1) == 3  