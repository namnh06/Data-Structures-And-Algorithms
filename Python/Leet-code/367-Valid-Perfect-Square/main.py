class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary Search Solution
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        if num == 1:
            return True
        
        left, right = 1, num // 2
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == num:
                return True
            elif mid_squared > num:
                right = mid - 1
            else:
                left = mid + 1
            
        return False
    
# Instantiate the solution object
s = Solution()

# Test case 1: num = 1 (edge case)
assert s.isPerfectSquare(1) == True, "Test case 1 failed"

# Test case 2: Small perfect square
assert s.isPerfectSquare(4) == True, "Test case 2 failed"  # 2^2 = 4

# Test case 3: Small non-perfect square
assert s.isPerfectSquare(5) == False, "Test case 3 failed"

# Test case 4: Larger perfect square
assert s.isPerfectSquare(16) == True, "Test case 4 failed"  # 4^2 = 16

# Test case 5: Larger non-perfect square
assert s.isPerfectSquare(14) == False, "Test case 5 failed"

# Test case 6: Very large perfect square
assert s.isPerfectSquare(1000000) == True, "Test case 6 failed"  # 1000^2 = 1000000

# Test case 7: Very large non-perfect square
assert s.isPerfectSquare(1000001) == False, "Test case 7 failed"

# Test case 8: Another perfect square
assert s.isPerfectSquare(49) == True, "Test case 8 failed"  # 7^2 = 49

# Test case 9: Another non-perfect square
assert s.isPerfectSquare(50) == False, "Test case 9 failed"

# Test case 10: Testing upper bound of integer
assert s.isPerfectSquare(2147395600) == True, "Test case 10 failed"  # 46340^2 = 2147395600

print("All test cases passed.")