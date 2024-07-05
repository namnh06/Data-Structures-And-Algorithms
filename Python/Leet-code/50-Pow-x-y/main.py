class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Brute-force Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # answer: int = 1
        # for i in range(abs(n)):
        #     answer *= x
        
        # if n < 0:
        #     return 1/answer
        
        # return answer

        # Binary Exponentiation
        # Time Complexity: O(log |n|)
        # Space Complexity: O(1)
        answer: int = 1
        abs_n: int = abs(n)
        while abs_n > 0:
            if abs_n % 2 == 1:
                answer *= x
            x *= x
            abs_n //= 2
        
        if n < 0:
            return 1/answer
        return answer


# Instantiate the solution object
s = Solution()

# Test case 1: Positive exponent
assert s.myPow(2.0, 10) == 1024.0, "Test case 1 failed"  # 2^10 = 1024

# Test case 2: Negative exponent
assert s.myPow(2.0, -2) == 0.25, "Test case 2 failed"    # 2^-2 = 1/4 = 0.25

# Test case 3: Zero exponent
assert s.myPow(2.0, 0) == 1.0, "Test case 3 failed"      # 2^0 = 1

# Test case 4: One as the base
assert s.myPow(1.0, 1000) == 1.0, "Test case 4 failed"   # 1^1000 = 1

# Test case 5: Negative base with even exponent
assert s.myPow(-2.0, 4) == 16.0, "Test case 5 failed"    # (-2)^4 = 16

# Test case 6: Negative base with odd exponent
assert s.myPow(-2.0, 3) == -8.0, "Test case 6 failed"    # (-2)^3 = -8

# Test case 7: Fractional base with positive exponent
assert s.myPow(0.5, 3) == 0.125, "Test case 7 failed"    # 0.5^3 = 0.125

# Test case 8: Fractional base with negative exponent
assert s.myPow(0.5, -2) == 4.0, "Test case 8 failed"     # 0.5^-2 = 4

# Test case 9: Large positive exponent
assert s.myPow(2.0, 31) == 2147483648.0, "Test case 9 failed"  # 2^31

# Test case 10: Large negative exponent
assert abs(s.myPow(2.0, -31) - 4.656612877414201e-10) < 1e-15, "Test case 10 failed"  # 2^-31

print("All test cases passed.")