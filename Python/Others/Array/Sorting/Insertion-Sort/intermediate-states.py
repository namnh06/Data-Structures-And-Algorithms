# https://neetcode.io/problems/insertionSort
from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        
    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __repr__(self):
        return f'Pair({self.key}, "{self.value}")'

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result: List[List[Pair]] = []
        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1
            result.append(pairs[:])
        return result

def compare_result(result: List[List[Pair]], expected: List[List[Pair]]) -> bool:
    if len(result) != len(expected):
        return False
    for res, exp in zip(result, expected):
        if len(res) != len(exp):
            return False
        for r, e in zip(res, exp):
            if not (r == e):
                return False
    return True

# Test Cases
pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
expected_output = [
    [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")], 
    [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")], 
    [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 1 failed."

pairs = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
expected_output = [
    [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")], 
    [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")], 
    [Pair(2, "dog"), Pair(3, "cat"), Pair(3, "bird")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 2 failed."

pairs = [Pair(1, "one")]
expected_output = [
    [Pair(1, "one")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 3 failed."

pairs = [Pair(4, "d"), Pair(3, "c"), Pair(2, "b"), Pair(1, "a")]
expected_output = [
    [Pair(4, "d"), Pair(3, "c"), Pair(2, "b"), Pair(1, "a")],
    [Pair(3, "c"), Pair(4, "d"), Pair(2, "b"), Pair(1, "a")],
    [Pair(2, "b"), Pair(3, "c"), Pair(4, "d"), Pair(1, "a")],
    [Pair(1, "a"), Pair(2, "b"), Pair(3, "c"), Pair(4, "d")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 4 failed."

pairs = [Pair(10, "ten"), Pair(8, "eight"), Pair(6, "six"), Pair(4, "four"), Pair(2, "two")]
expected_output = [
    [Pair(10, "ten"), Pair(8, "eight"), Pair(6, "six"), Pair(4, "four"), Pair(2, "two")],
    [Pair(8, "eight"), Pair(10, "ten"), Pair(6, "six"), Pair(4, "four"), Pair(2, "two")],
    [Pair(6, "six"), Pair(8, "eight"), Pair(10, "ten"), Pair(4, "four"), Pair(2, "two")],
    [Pair(4, "four"), Pair(6, "six"), Pair(8, "eight"), Pair(10, "ten"), Pair(2, "two")],
    [Pair(2, "two"), Pair(4, "four"), Pair(6, "six"), Pair(8, "eight"), Pair(10, "ten")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 5 failed."

pairs = [Pair(1, "apple"), Pair(2, "banana"), Pair(3, "cherry"), Pair(4, "date")]
expected_output = [
    [Pair(1, "apple"), Pair(2, "banana"), Pair(3, "cherry"), Pair(4, "date")],
    [Pair(1, "apple"), Pair(2, "banana"), Pair(3, "cherry"), Pair(4, "date")],
    [Pair(1, "apple"), Pair(2, "banana"), Pair(3, "cherry"), Pair(4, "date")],
    [Pair(1, "apple"), Pair(2, "banana"), Pair(3, "cherry"), Pair(4, "date")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 6 failed."

pairs = [Pair(2, "a"), Pair(2, "b"), Pair(2, "c")]
expected_output = [
    [Pair(2, "a"), Pair(2, "b"), Pair(2, "c")],
    [Pair(2, "a"), Pair(2, "b"), Pair(2, "c")],
    [Pair(2, "a"), Pair(2, "b"), Pair(2, "c")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 7 failed."

pairs = [Pair(5, "z"), Pair(4, "y"), Pair(5, "x"), Pair(4, "w"), Pair(5, "v")]
expected_output = [
    [Pair(5, "z"), Pair(4, "y"), Pair(5, "x"), Pair(4, "w"), Pair(5, "v")],
    [Pair(4, "y"), Pair(5, "z"), Pair(5, "x"), Pair(4, "w"), Pair(5, "v")],
    [Pair(4, "y"), Pair(5, "z"), Pair(5, "x"), Pair(4, "w"), Pair(5, "v")],
    [Pair(4, "y"), Pair(4, "w"), Pair(5, "z"), Pair(5, "x"), Pair(5, "v")],
    [Pair(4, "y"), Pair(4, "w"), Pair(5, "z"), Pair(5, "x"), Pair(5, "v")]
]
assert compare_result(Solution().insertionSort(pairs), expected_output), "Test case 8 failed."

print("All test cases passed.")