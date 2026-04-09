import unittest
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        origin_color = image[sr][sc]
        
        if origin_color == color:
            return image
        
        def dfs(row: int, column: int) -> None:
            if row < 0 or column < 0 or row >= rows or column >= cols:
                return
            
            if image[row][column] != origin_color:
                return
            
            image[row][column] = color
            
            dfs(row - 1, column)
            dfs(row + 1, column)
            dfs(row, column - 1)
            dfs(row, column + 1)
            
        dfs(sr, sc)
        return image

class TestFloodFill(unittest.TestCase):
    def test_case_1(self) -> None:
        solution = Solution()
        result = solution.floodFill(
            [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
        )
        
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        
        self.assertEqual(result, expected)