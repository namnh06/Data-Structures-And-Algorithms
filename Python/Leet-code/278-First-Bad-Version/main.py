# https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
        
def isBadVersion(version: int) -> bool:
    global first_bad_version
    return version >= first_bad_version


s = Solution()

# Test cases
first_bad_version = 2
assert s.firstBadVersion(3) == 2  # Test case n = 3, bad = 2

first_bad_version = 4
assert s.firstBadVersion(5) == 4  # Given that versions 4 and 5 are bad
assert s.firstBadVersion(10) == 4 # Given that versions 4 through 10 are bad
assert s.firstBadVersion(100) == 4 # Larger range

first_bad_version = 1
assert s.firstBadVersion(1) == 1  # If the first version is bad

first_bad_version = 2
assert s.firstBadVersion(2) == 2  # If the second version is bad in a 2-element array

first_bad_version = 1
assert s.firstBadVersion(3) == 1  # If the first version is bad in a 3-element array

first_bad_version = 3
assert s.firstBadVersion(3) == 3  # If the last version is bad in a 3-element array

print("All test cases pass")