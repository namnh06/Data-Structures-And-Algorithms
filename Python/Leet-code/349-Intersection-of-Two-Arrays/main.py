from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Set Solution
        # Time Complexity: O(n+m)
        # Space Complexity: O(n)
        nums1_set: Set(int) = set()
        result: List[int] = list()
        for num in nums1:
            nums1_set.add(num)
            
        for num in nums2:
            if num in nums1_set:
                result.append(num)
                nums1_set.remove(num)
                
        return result
    
if __name__ == "__main__":
    assert Solution().intersection([1,1,2,2],[2,2]) == [2], "Test case 1 failed."
    assert Solution().intersection([1,1,2,2],[2,2,1]) == [1,2] or [2,1], "Test case 2 failed."
    assert Solution().intersection([4,9,5],[9,4,9,8,4]) == [4,9] or [9,4], "Test case 3 failed."
    print("All test cases passed.")