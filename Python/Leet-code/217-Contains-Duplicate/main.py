from typing import List, Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        unique_nums: Set[int] = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False
    
# Test cases
assert Solution().containsDuplicate([1, 2, 3, 4]) == False, "Test case 1 failed"
assert Solution().containsDuplicate([1, 2, 3, 1]) == True, "Test case 2 failed"
assert Solution().containsDuplicate([1, 1, 1, 1]) == True, "Test case 3 failed"
assert Solution().containsDuplicate([]) == False, "Test case 4 failed"
assert Solution().containsDuplicate([1]) == False, "Test case 5 failed"
assert Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False, "Test case 6 failed"
assert Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]) == True, "Test case 7 failed"

print("All test cases passed.")