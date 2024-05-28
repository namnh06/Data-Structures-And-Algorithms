class Solution():
    def merge_sort(self, nums: list[int]) -> list[int]:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        n:int = len(nums)
        if n <= 1:
            return nums
        mid: int = n // 2
        leftHalf: list[int] = nums[:mid] # Time Complexity: O(n)
        rightHalf: list[int] = nums[mid:] # Time Complexity: O(n)
        
        leftSorted = self.merge_sort(leftHalf)
        rightSorted = self.merge_sort(rightHalf)
        
        return self.merge(leftSorted, rightSorted)
    
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result: list[int] = [] # Space Complexity: O(n)
        leftIndex: int = 0
        rightIndex: int = 0
        
        # Time Complexity: O(log n)
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                result.append(left[leftIndex])
                leftIndex += 1
            else:
                result.append(right[rightIndex])
                rightIndex += 1
        
        while leftIndex < len(left):
            result.append(left[leftIndex])
            leftIndex += 1
            
        while rightIndex < len(right):
            result.append(right[rightIndex])
            rightIndex += 1
        
        return result
        
    
if __name__ == "__main__":
    s = Solution()
    
    result = s.merge_sort([1, 3, 2])
    assert result == [1, 2, 3]
    
    result = s.merge_sort([1, 3, 2, -1])
    assert result == [-1, 1, 2, 3]
    
    result = s.merge_sort([38, 27, 43, 3, 9, 82, 10])
    assert result == [3, 9, 10, 27, 38, 43, 82]