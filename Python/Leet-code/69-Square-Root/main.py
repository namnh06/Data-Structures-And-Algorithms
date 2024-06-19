# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def square_root(self, x: int) -> int:
        if x <= 1:
            return x
        
        left: int = 0
        right: int = x//2 + 1
        
        while left <= right:
            mid: int = (left + right) // 2
            
            if mid == x//mid:
                return mid
            
            if mid > x//mid:
                right = mid - 1
            else:
                left = mid + 1
                
        return right

if __name__ == "__main__":
    
    assert Solution().square_root(0) == 0
    assert Solution().square_root(1) == 1
    assert Solution().square_root(2) == 1
    assert Solution().square_root(3) == 1
    assert Solution().square_root(4) == 2
    assert Solution().square_root(5) == 2
    assert Solution().square_root(6) == 2
    assert Solution().square_root(8) == 2
    assert Solution().square_root(9) == 3
    assert Solution().square_root(2147395600) == 46340
    
    print("All test cases pass")