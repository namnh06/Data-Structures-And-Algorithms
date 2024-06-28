# https://leetcode.com/problems/find-k-closest-elements/

from typing import List, Tuple
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Two Pointer
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # left, right = 0, len(arr) - 1
        # while right - left + 1 > k:
        #     if abs(arr[left] - x) <= abs(arr[right] - x):
        #         right -= 1
        #     else:
        #         left += 1
        # return arr[left:right+1]

        # Binary Search
        # Time Complexity: O(log n + k)
        # Space Complexity: O(1)
        # left, right = 0, len(arr) - 1

        # while left < right: # O(log n)
        #     mid = (left + right) // 2

        #     if arr[mid] > x:
        #         right = mid
        #     else:
        #         left = mid + 1

        # left = right - 1

        # while k > 0: O(k)
        #     if left < 0:
        #         right += 1
        #     elif right > len(arr) - 1:
        #         left -= 1
        #     elif abs(arr[left] - x) <= abs(arr[right] - x):
        #         left -= 1
        #     else:
        #         right += 1
        #     k -= 1
        
        # return arr[left+1:right]

        # Binary Search version 2
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        # left, right = 0, len(arr) - k
        
        # while left < right: # O(log(n-k))
        #     mid = (left + right) // 2

        #     if x - arr[mid] <= arr[mid+k] - x:
        #         right -= 1
        #     else:
        #         left += 1

        # return arr[left:left+k]

        # Heap (Priority Queue)
        # Time Complexity: O(n log k)
        # Space Complexity: O(k)
        max_heap: List[Tuple[int, int]] = [] # O(k)
        # -difference, -num
        for num in arr: # O(n)
            heapq.heappush(max_heap, ((-abs(num-x)), -num))

            if len(max_heap) > k: # O(log k)
                heapq.heappop(max_heap)

        result = sorted(-num for _, num in max_heap) # O (k log k)
        return result
    
s = Solution()

assert s.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4], "Test case 1 failed"
assert s.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4], "Test case 2 failed"
assert s.findClosestElements([1, 2, 3, 4, 5], 4, 6) == [2, 3, 4, 5], "Test case 3 failed"
assert s.findClosestElements([1, 2, 3, 4, 5], 1, 3) == [3], "Test case 4 failed"
assert s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10], "Test case 5 failed"
assert s.findClosestElements([1, 1, 1, 10, 10, 10], 2, 9) == [10, 10], "Test case 6 failed"
assert s.findClosestElements([1, 1, 1, 10, 10, 10], 3, 9) == [10, 10, 10], "Test case 7 failed"
assert s.findClosestElements([1, 1, 1, 10, 10, 10], 3, 10) == [10, 10, 10], "Test case 8 failed"
assert s.findClosestElements([1, 2, 2, 2, 5, 5, 5, 6], 3, 3) == [2, 2, 2], "Test case 9 failed"

print("All test cases passed")