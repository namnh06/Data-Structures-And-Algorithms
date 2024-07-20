from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = prices[0]
        max_profit: int = 0
        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0, "Test case 2 failed"
assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4, "Test case 3 failed"
assert Solution().maxProfit([1, 2, 3, 1, 5]) == 4, "Test case 4 failed"
assert Solution().maxProfit([1]) == 0, "Test case 5 failed"
assert Solution().maxProfit([2, 4, 1]) == 2, "Test case 6 failed"

print("All test cases passed.")