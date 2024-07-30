class Solution:
    def calPoints(self, operations: str) -> int:
        records: List[int] = []
        for o in operations:
            if o == 'C':
                records.pop()
            elif o == 'D':
                records.append(records[-1] * 2)
            elif o == '+':
                records.append(records[-1] + records[-2])
            else:
                records.append(int(o))
        return sum(records)

def test_calPoints():
    solution = Solution()
    
    # Test case 1
    operations = ["5", "2", "C", "D", "+"]
    expected = 30
    assert solution.calPoints(operations) == expected, f"Test case 1 failed: expected {expected}, got {solution.calPoints(operations)}"
    
    # Test case 2
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    expected = 27
    assert solution.calPoints(operations) == expected, f"Test case 2 failed: expected {expected}, got {solution.calPoints(operations)}"
    
    # Test case 3
    operations = ["1", "C"]
    expected = 0
    assert solution.calPoints(operations) == expected, f"Test case 3 failed: expected {expected}, got {solution.calPoints(operations)}"
    
    # Test case 4
    operations = ["5", "2", "C", "D", "+", "3", "+", "C"]
    expected = 33
    assert solution.calPoints(operations) == expected, f"Test case 4 failed: expected {expected}, got {solution.calPoints(operations)}"
    
    # Test case 5: Complex sequence
    operations = ["5", "2", "4", "C", "D", "9", "+", "+", "C", "5", "D"]
    expected = 48
    assert solution.calPoints(operations) == expected, f"Test case 5 failed: expected {expected}, got {solution.calPoints(operations)}"
    
    print("All test cases passed.")

test_calPoints()