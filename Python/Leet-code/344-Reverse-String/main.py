class Solution:
    def reverseString(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
def test_reverseString():
    solution = Solution()
    
    # Test case 1
    s = ["h", "e", "l", "l", "o"]
    expected = ["o", "l", "l", "e", "h"]
    solution.reverseString(s)
    assert s == expected, f"Test case 1 failed: expected {expected}, got {s}"
    
    # Test case 2
    s = ["H", "a", "n", "n", "a", "h"]
    expected = ["h", "a", "n", "n", "a", "H"]
    solution.reverseString(s)
    assert s == expected, f"Test case 2 failed: expected {expected}, got {s}"
    
    # Test case 3: Single character
    s = ["a"]
    expected = ["a"]
    solution.reverseString(s)
    assert s == expected, f"Test case 3 failed: expected {expected}, got {s}"
    
    # Test case 4: Two characters
    s = ["a", "b"]
    expected = ["b", "a"]
    solution.reverseString(s)
    assert s == expected, f"Test case 4 failed: expected {expected}, got {s}"
    
    # Test case 5: Empty list
    s = []
    expected = []
    solution.reverseString(s)
    assert s == expected, f"Test case 5 failed: expected {expected}, got {s}"
    
    # Test case 6: Palindrome
    s = ["m", "a", "d", "a", "m"]
    expected = ["m", "a", "d", "a", "m"]
    solution.reverseString(s)
    assert s == expected, f"Test case 6 failed: expected {expected}, got {s}"
    
    print("All test cases passed.")

test_reverseString()