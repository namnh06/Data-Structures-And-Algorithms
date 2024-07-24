from typing import List
class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
    
# Test cases
assert Solution().insertionSort([]) == [], "Test case 1 failed."
assert Solution().insertionSort([3, 2, 1]) == [1, 2, 3], "Test case 2 failed."
assert Solution().insertionSort([2, 3, 1]) == [1, 2, 3], "Test case 3 failed."
assert Solution().insertionSort([2, 1, 3]) == [1, 2, 3], "Test case 4 failed."
assert Solution().insertionSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 5 failed."
assert Solution().insertionSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 6 failed."
print("All test cases passed.")

