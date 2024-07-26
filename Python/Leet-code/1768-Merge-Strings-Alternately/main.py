from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        result: List[str] = []
        pointer: int = 0
        while n > pointer and m > pointer:
            result.append(word1[pointer])
            result.append(word2[pointer])
            pointer += 1
        
        result.append(word1[pointer:])
        result.append(word2[pointer:])
        return ''.join(result)

def test_mergeAlternately():
    solution = Solution()
    
    # Test case 1: Equal length strings
    word1 = "abc"
    word2 = "pqr"
    expected = "apbqcr"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 1 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 2: word1 is longer than word2
    word1 = "abcd"
    word2 = "pq"
    expected = "apbqcd"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 2 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 3: word2 is longer than word1
    word1 = "ab"
    word2 = "pqrs"
    expected = "apbqrs"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 3 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 4: word1 is empty
    word1 = ""
    word2 = "xyz"
    expected = "xyz"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 4 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 5: word2 is empty
    word1 = "abc"
    word2 = ""
    expected = "abc"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 5 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 6: Both words are empty
    word1 = ""
    word2 = ""
    expected = ""
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 6 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 7: Single character words
    word1 = "a"
    word2 = "b"
    expected = "ab"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 7 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    # Test case 8: Long strings
    word1 = "abcdefghij"
    word2 = "klmnopqrst"
    expected = "akblcmdneofpgqhrisjt"
    assert solution.mergeAlternately(word1, word2) == expected, f"Test case 8 failed: expected {expected}, got {solution.mergeAlternately(word1, word2)}"
    
    print("All test cases passed.")

test_mergeAlternately()