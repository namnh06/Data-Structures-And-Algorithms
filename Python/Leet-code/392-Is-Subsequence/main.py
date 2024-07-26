import unittest

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        s_pointer, t_pointer = 0, 0
        while s_pointer < n and t_pointer < m:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == n

class TestIsSubsequence(unittest.TestCase):
    def test_simple_cases(self):
        self.assertTrue(Solution().isSubsequence("a", "ahbgdc"))
        self.assertTrue(Solution().isSubsequence("axc", "ahxbgdc"))
        self.assertFalse(Solution().isSubsequence("axd", "ahbgdc"))

    def test_empty_strings(self):
        self.assertTrue(Solution().isSubsequence("", "ahbgdc"))
        self.assertTrue(Solution().isSubsequence("", ""))

    def test_equal_strings(self):
        self.assertTrue(Solution().isSubsequence("abc", "abc"))

    def test_long_strings(self):
        self.assertTrue(Solution().isSubsequence("abcde", "ahbgcdcfe"))
        self.assertFalse(Solution().isSubsequence("abcde", "ahbgdcf"))

    def test_repeated_characters(self):
        self.assertTrue(Solution().isSubsequence("aaa", "aaab"))
        self.assertFalse(Solution().isSubsequence("aaa", "aab"))

if __name__ == '__main__':
    unittest.main()