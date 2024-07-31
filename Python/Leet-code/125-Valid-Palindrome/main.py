from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TC: O(n)
        # SC: O(n)
        # s_formatted: List[str] = [c.lower() for c in s if c.isalnum()]
        # for c in s:
        #     if c.isalnum():
        #         s_formatted.append(c.lower())

        # left, right = 0, len(s_formatted)-1
        # while left < right:
        #     if s_formatted[left] != s_formatted[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
    
        # TC: O(n)
        # SC: O(1)
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1
                
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
            left += 1
            right -= 1
                
        return True

def test_isPalindrome():
    solution = Solution()
    
    # Test case 1: Simple palindrome
    s = "A man, a plan, a canal: Panama"
    expected = True
    assert solution.isPalindrome(s) == expected, f"Test case 1 failed: expected {expected}, got {solution.isPalindrome(s)}"
    
    # Test case 2: Not a palindrome
    s = "race a car"
    expected = False
    assert solution.isPalindrome(s) == expected, f"Test case 2 failed: expected {expected}, got {solution.isPalindrome(s)}"
    
    # Test case 3: Empty string
    s = ""
    expected = True
    assert solution.isPalindrome(s) == expected, f"Test case 3 failed: expected {expected}, got {solution.isPalindrome(s)}"
    
    # Test case 4: Single character
    s = "a"
    expected = True
    assert solution.isPalindrome(s) == expected, f"Test case 4 failed: expected {expected}, got {solution.isPalindrome(s)}"
    
    # Test case 5: Mixed alphanumeric
    s = "0P"
    expected = False
    assert solution.isPalindrome(s) == expected, f"Test case 5 failed: expected {expected}, got {solution.isPalindrome(s)}"
    
    print("All test cases passed.")

test_isPalindrome()