class Solution:
    def quick_sort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        pivot: int = nums[0]
        left: list[int] = []
        right: list[int] = []
        middle: list[int] = []
        # Space Complexity: O(n)
        for num in nums: # Time Complexity: O(n)
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        
        # Time Complexity: Average O(n log n), Worst O(n^2)
        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def quick_sort_in_place(self, nums: list[int]) -> list[int]:
        def sort(low, high):
            if low < high:
                pivot_idx = partition(low, high)
                sort(low, pivot_idx -1)
                sort(pivot_idx + 1, high)
        
        def partition(low, high):
            pivot = nums[high]
            i = low
            
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        
        sort(0, len(nums) - 1)
        return nums
if __name__ == "__main__":
    s = Solution()
    
    result = s.quick_sort([1, 3, 2])
    assert result == [1, 2, 3]
    
    result = s.quick_sort([-1, 8, 2, 6, 7, 0, 1, 3, 2, 9, -2])
    assert result == [-2, -1, 0, 1, 2, 2, 3, 6, 7, 8, 9]
    
    nums: list[int] = [20, 6, 8, 53, 23, 87, 42, 19]
    result = s.quick_sort_in_place(nums)