# https://leetcode.com/problems/valid-anagram/description/
from typing import Dict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # s_indices: Dict[str, int] = {}
        # t_indices: Dict[str, int] = {}
        
        # for i in range(len(s)):
        #     s_indices[s[i]] = s_indices.get(s[i], 0) + 1
        #     t_indices[t[i]] = t_indices.get(t[i], 0) + 1
        
        # Use Counter
        s_indices: Dict[str, int] = Counter(s)
        t_indices: Dict[str, int] = Counter(t)

        return s_indices == t_indices


if __name__ == "__main__":
    assert Solution().isAnagram("anagram", "nagaram") == True, "Test case 1 failed"
    assert Solution().isAnagram("rat", "car") == False, "Test case 2 failed"
    assert Solution().isAnagram("a", "a") == True, "Test case 3 failed"
    assert Solution().isAnagram("a", "b") == False, "Test case 4 failed"

    print("All test cases passed.")