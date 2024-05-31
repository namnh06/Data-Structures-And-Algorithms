class Solution:
    def fibonacci(self, n: int, memo: dict = None) -> int:
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1: 
            return n
        memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return memo[n]
    
if __name__ == "__main__":
    s = Solution()
    
    result = s.fibonacci(5)
    assert result == 5
    
    result = s.fibonacci(10)
    assert result == 55
    
    