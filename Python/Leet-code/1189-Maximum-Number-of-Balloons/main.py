from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = Counter("balloon")
        text_count = Counter(text)
        return min(text_count[char] // balloon_count[char] for char in balloon_count)

def test_maxNumberOfBalloons():
    solution = Solution()
    
    # Test case 1
    text = "nlaebolko"
    expected = 1
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 1 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 2
    text = "loonbalxballpoon"
    expected = 2
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 2 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 3
    text = "leetcode"
    expected = 0
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 3 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 4: Multiple instances
    text = "balloonballoonballoon"
    expected = 3
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 4 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 5: Single character multiple times
    text = "llllooobbbnnn"
    expected = 0
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 5 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 6: Enough characters but not all needed ones
    text = "balon"
    expected = 0
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 6 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    # Test case 7: Just enough characters to form one "balloon"
    text = "balonbalonlo"
    expected = 1
    assert solution.maxNumberOfBalloons(text) == expected, f"Test case 7 failed: expected {expected}, got {solution.maxNumberOfBalloons(text)}"
    
    print("All test cases passed.")

test_maxNumberOfBalloons()