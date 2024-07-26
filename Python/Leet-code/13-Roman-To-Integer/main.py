import unittest
from typing import Dict

class Solution:
    def romanToInt(self, s: str) -> int:
        roman: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        result: int = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                result += roman[s[i]] - 2 * roman[s[i-1]]
            else:
                result += roman[s[i]]
        return result

class TestRomanToInt(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(Solution().romanToInt("I"), 1)
        self.assertEqual(Solution().romanToInt("V"), 5)
        self.assertEqual(Solution().romanToInt("X"), 10)
        self.assertEqual(Solution().romanToInt("L"), 50)
        self.assertEqual(Solution().romanToInt("C"), 100)
        self.assertEqual(Solution().romanToInt("D"), 500)
        self.assertEqual(Solution().romanToInt("M"), 1000)

    def test_additive_cases(self):
        self.assertEqual(Solution().romanToInt("II"), 2)
        self.assertEqual(Solution().romanToInt("III"), 3)
        self.assertEqual(Solution().romanToInt("VI"), 6)
        self.assertEqual(Solution().romanToInt("XII"), 12)
        self.assertEqual(Solution().romanToInt("XXV"), 25)

    def test_subtractive_cases(self):
        self.assertEqual(Solution().romanToInt("IV"), 4)
        self.assertEqual(Solution().romanToInt("IX"), 9)
        self.assertEqual(Solution().romanToInt("XL"), 40)
        self.assertEqual(Solution().romanToInt("XC"), 90)
        self.assertEqual(Solution().romanToInt("CD"), 400)
        self.assertEqual(Solution().romanToInt("CM"), 900)

    def test_complex_cases(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)
        self.assertEqual(Solution().romanToInt("MMXXI"), 2021)

if __name__ == '__main__':
    unittest.main()