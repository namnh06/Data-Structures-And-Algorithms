import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = ""
        if len(strs) == 0:
            return result

        # TC: O(n*m)
        # SC: O(m)
        # for i in range(len(strs[0])):
        #     c: str = strs[0][i]
        #     for s in strs:
        #         if i >= len(s) or s[i] != c:
        #             return result
        #     result += c
        
        # TC: O(n)
        # SC: O(1)
        for char in zip(*strs):
            if len(set(char)) == 1:
                result += char[0]
            else:
                return result
        return result

class TestLongestCommonPrefix(unittest.TestCase):

    def test_1_simple_cases(self):
        self.assertEqual(Solution().longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(Solution().longestCommonPrefix(["dog","racecar","car"]), "")

    def test_2_single_string(self):
        self.assertEqual(Solution().longestCommonPrefix(["a"]), "a")

    def test_3_empty_list(self):
        self.assertEqual(Solution().longestCommonPrefix([]), "")

    def test_4_empty_strings(self):
        self.assertEqual(Solution().longestCommonPrefix(["", "", ""]), "")

    def test_5_long_strings(self):
        self.assertEqual(Solution().longestCommonPrefix(["abcdefgh", "abcdefg", "abcdef"]), "abcdef")

    def test_6_no_common_prefix(self):
        self.assertEqual(Solution().longestCommonPrefix(["apple", "banana", "cherry"]), "")

if __name__ == '__main__':
    unittest.main()