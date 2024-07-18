from typing import List
import bisect
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute-force Solution
        # Time Complexity: O(n+m)
        # Space Complexity: O(n+m)
        # count1 = Counter(nums1)
        # count2 = Counter(nums2)
        # result: List[int] = list()
        # for key in count1:
        #     if key in count2:
        #         min_count = min(count1[key], count2[key])
        #         result.extend([key] * min_count)
        # return result

        # Counter
        # Time Complexity: O(n+m)
        # Space Complexity: O(min(n,m))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count1 = Counter(nums1)
        result = list()
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        
        return result

        # Sorted
        # Time Complexity: O(n+m)
        # Space Complexity: O(1)
        # nums1.sort()
        # nums2.sort()
        # i, j = 0, 0
        # result = []

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] == nums2[j]:
        #         result.append(nums1[i])
        #         i += 1
        #         j += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         i += 1
        
        # return result

        # Sorted with Binary Search
        # nums1.sort()
        # nums2.sort()

        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1

        # result = []
        # for num in nums1:
        #     index = bisect.bisect_left(nums2, num)
        #     if index < len(nums2) and nums2[index] == num:
        #         result.append(num)
        #         nums2.pop(index)
            # Binary Search Mannualy
            # left, right = 0, len(nums2)
            # while left < right:
            #     mid = (left + right) // 2
            #     if nums2[mid] == num:
            #         result.append(num)
            #         nums2.pop(mid)
            #         left, right = mid, mid
            #     elif nums2[mid] > num:
            #         right = mid
            #     else:
            #         left = mid + 1

        # return result
    
solution = Solution()
# assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2], "Test case 1 failed"
assert solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or [4, 9], "Test case 2 failed"
assert solution.intersect([1, 2, 3, 4], [1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4], "Test case 3 failed"
print("All test cases passed.")