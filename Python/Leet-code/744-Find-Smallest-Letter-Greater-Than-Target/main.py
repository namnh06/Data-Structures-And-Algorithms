from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Brute-force Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # for c in letters:
        #     if c > target:
        #         return c
        # return letters[0]
        
        # Binary Search Solution
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        n = len(letters)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        if letters[left] <= target:
            return letters[0]
        
        return letters[left]

# Instantiate the solution object
s = Solution()

# Test case 1: Target letter is in the middle of the array
assert s.nextGreatestLetter(["c", "f", "j"], "a") == "c", "Test case 1 failed"

# Test case 2: Target letter is less than all elements in the array
assert s.nextGreatestLetter(["c", "f", "j"], "c") == "f", "Test case 2 failed"

# Test case 3: Target letter is between elements in the array
assert s.nextGreatestLetter(["c", "f", "j"], "d") == "f", "Test case 3 failed"

# Test case 4: Target letter is greater than all elements in the array
assert s.nextGreatestLetter(["c", "f", "j"], "g") == "j", "Test case 4 failed"

# Test case 5: Target letter is the last element in the array
assert s.nextGreatestLetter(["c", "f", "j"], "j") == "c", "Test case 5 failed"

# Test case 6: All elements in the array are the same
assert s.nextGreatestLetter(["c", "c", "c"], "c") == "c", "Test case 6 failed"

# Test case 7: Large array with wrap-around
assert s.nextGreatestLetter(["a", "b", "d", "e", "h", "i", "j", "k"], "k") == "a", "Test case 7 failed"

# Test case 8: Single element array
assert s.nextGreatestLetter(["a"], "a") == "a", "Test case 8 failed"

print("All test cases passed.")