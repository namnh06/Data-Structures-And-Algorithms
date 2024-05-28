# Bubble Sort
class Solution:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n): # Time Complexity: O(n)
            swapped: bool = False
            for j in range(0, n-i-1): # Time Complexity: O(n)
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        return nums
    
if __name__ == "__main__":
    s = Solution()
    
    # result = s.bubble_sort([1, 3, 2])
    # assert result == [1, 2, 3]
    
    result = s.bubble_sort([6, 4, 1, 5, 3, 2])
    print(result)
    assert result == [1, 2, 3, 4, 5, 6]
