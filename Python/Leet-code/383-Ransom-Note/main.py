from typing import Dict
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazine: Dict[str, int] = Counter(magazine)
        
        # for c in ransomNote:
        #     if c in magazine and magazine[c] > 0:
        #         magazine[c] -= 1
        #     else:
        #         return False
        
        magazine_count = Counter(magazine)
        ransome_note_count = Counter(ransomNote)
        
        for char, count in ransome_note_count.items():
            if magazine_count[char] < count:
                return False
            
        return True

def test_canConstruct():
    solution = Solution()
    
    # Test case 1
    ransomNote = "a"
    magazine = "b"
    expected = False
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 1 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 2
    ransomNote = "aa"
    magazine = "ab"
    expected = False
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 2 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 3
    ransomNote = "aa"
    magazine = "aab"
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 3 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 4: ransomNote is empty
    ransomNote = ""
    magazine = "a"
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 4 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 5: magazine is empty
    ransomNote = "a"
    magazine = ""
    expected = False
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 5 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 6: ransomNote equals magazine
    ransomNote = "abc"
    magazine = "abc"
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 6 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    # Test case 7: magazine has extra characters
    ransomNote = "abc"
    magazine = "abcd"
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected, f"Test case 7 failed: expected {expected}, got {solution.canConstruct(ransomNote, magazine)}"
    
    print("All test cases passed.")

test_canConstruct()