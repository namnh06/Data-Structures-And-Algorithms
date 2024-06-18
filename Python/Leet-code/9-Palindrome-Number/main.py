class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Best Conceivable Runtime: O(log n)
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        right: int = 0
        while x > right:
            right = (right * 10) + (x % 10)
            x = x // 10
            
        return x == right or right // 10 == x
    
if __name__ == "__main__":
    s = Solution()
    
    # Test case 1: A positive palindrome number
    assert s.isPalindrome(121) == True
    
    # Test case 2: A positive non-palindrome number
    assert s.isPalindrome(123) == False
    
    # Test case 3: A single-digit number (always a palindrome)
    assert s.isPalindrome(7) == True
    
    # Test case 4: A negative number (never a palindrome)
    assert s.isPalindrome(-121) == False
    
    # Test case 5: A number ending in zero (except zero itself)
    assert s.isPalindrome(10) == False
    
    # Test case 6: Zero (a palindrome)
    assert s.isPalindrome(0) == True
    
    # Test case 7: A large palindrome number
    assert s.isPalindrome(1234321) == True
    
    # Test case 8: A large non-palindrome number
    assert s.isPalindrome(123456) == False
    
    print("All test cases pass")
