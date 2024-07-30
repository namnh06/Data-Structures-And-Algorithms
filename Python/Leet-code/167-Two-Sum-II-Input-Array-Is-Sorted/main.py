from typing import List, Dict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Hashmap
        # TC: O(n)
        # SC: O(n)
        # numbers_dict: Dict[int, int] = {}
        # for i in range(len(numbers)):
        #     if numbers[i] in numbers_dict:
        #         return [numbers_dict[numbers[i]]+1, i+1]
        #     numbers_dict[target-numbers[i]] = i
        # return [-1,-1]
        
        # Binary Search
        # TC: O(n log n)
        # SC: O(1)
        # for i in range(len(numbers)):
        #     temp = target - numbers[i]
        #     left, right = i+1, len(numbers)-1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if numbers[mid] == temp:
        #             return [i+1, mid+1]
        #         elif numbers[mid] > temp:
        #             right = mid - 1
        #         elif numbers[mid] < temp:
        #             left = mid + 1
        # return [-1,-1]
        
        # Two Pointers
        # TC: O(n)
        # SC: O(1)
        left, right = 0, len(numbers)-1
        while left < right:
            temp_sump = numbers[left] + numbers[right]
            if temp_sump == target:
                return [left+1, right+1]
            elif temp_sump > target:
                right -= 1
            elif temp_sump < target:
                left += 1
        return [-1, -1]

def test_twoSum():
    solution = Solution()
    
    # Test case 1: General case
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected, f"Test case 1 failed: expected {expected}, got {solution.twoSum(numbers, target)}"
    
    # Test case 2: Another general case
    numbers = [1, 2, 3, 4, 4]
    target = 8
    expected = [4, 5]
    assert solution.twoSum(numbers, target) == expected, f"Test case 2 failed: expected {expected}, got {solution.twoSum(numbers, target)}"
    
    # Test case 3: Target at the end
    numbers = [5, 25, 75]
    target = 100
    expected = [2, 3]
    assert solution.twoSum(numbers, target) == expected, f"Test case 3 failed: expected {expected}, got {solution.twoSum(numbers, target)}"
    
    # Test case 4: Negative numbers
    numbers = [-3, 4, 3, 90]
    target = 0
    expected = [1, 3]
    assert solution.twoSum(numbers, target) == expected, f"Test case 4 failed: expected {expected}, got {solution.twoSum(numbers, target)}"
    
    # Test case 5: Large numbers
    numbers = [2, 1000000000]
    target = 1000000002
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected, f"Test case 5 failed: expected {expected}, got {solution.twoSum(numbers, target)}"
    
    print("All test cases passed.")

test_twoSum()