# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        total: int = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        return total
    
if __name__ == '__main__':
    s = Solution()
    
    result = s.numJewelsInStones("aA", "aAAbbbb")
    assert result == 3