import heapq

class Solution():
    def asteroids_destroyed(self, mass: int, asteroids: list[int]) -> bool:
        # for asteroid in sorted(asteroids):
        #     if mass < asteroid:
        #         return False
            
        #     mass += asteroid
        # return True
        
        heapq.heapify(asteroids) # Time Complexity: O(n)
        while asteroids:
            smallest = heapq.heappop(asteroids) # Time Complexity: O(log n)
            if smallest > mass:
                return False
            
            mass += smallest
            
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        return True
    
if __name__ == "__main__":
    s = Solution()
    
    result = s.asteroids_destroyed(8, [9,11,1,1])
    assert result == True
    
    result = s.asteroids_destroyed(10, [3,9,19,5,21])
    assert result == True
    
    result = s.asteroids_destroyed(5, [4,9,23,4])
    assert result == False