# Example: Print all integer solutions to the equation a^3 + b^3 = c^3 + d^3 
# where a, b, c, and d are integers between 1 and 100

class Solution:
    def equationTriple(self):
        result_map = dict()
        for c in range(1,101):
            for d in range(1,101):
                sum_cd = c**3 + d**3
                if sum_cd not in result_map:
                    result_map[sum_cd] = []
                result_map[sum_cd].append((c,d))
                
        for sum_ab, pairs in result_map.items():
            for (a, b) in pairs:
                for (c, d) in pairs:
                    print(f"a:{a}, b:{b}, c:{c}, d:{d}")
                    
                    
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        return None
    
if __name__ == "__main__":
    s = Solution()
    
    s.equationTriple()