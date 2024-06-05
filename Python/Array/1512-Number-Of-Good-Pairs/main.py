from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # n: int = len(nums)
        answer: int = 0
        # Brute Force Solution
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             answer += 1

        # # Time Complexity: O(n^2)
        # # Space Complexity: O(1)
        # return answer

        # Hashmap Solution O(n)
        hashmap = dict()
        for num in nums:
            answer += hashmap.get(num, 0)
            hashmap[num] = hashmap.get(num, 0) + 1

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return answer

if __name__ == "__main__":
    s = Solution()
    
    result = s.numIdenticalPairs([1,2,3,1,1,3])
    assert result == 4
    
    result = s.numIdenticalPairs([1,1,1,1,1])
    assert result == 10