# Example: Given a smaller string s and a bigger string b, design an algorithm
# to find all permutations of the shorter string within the longer one. 
# Print the location of each permutation
# Constraint: len(s) < len(b)
from collections import Counter

class Solution:
    def permute_string(self, s: str, b: str) -> None:
        # Brute Force
        # Time Complexity: O(s!*b)
        # Space Complexity: O(s*s!)
        # # find all permutation of s
        # def backtrack(start):
        #     if start == len(s):
        #         s_permutation.append(s[:])
        #     else:
        #         for i in range(start, len(s)):
        #             s[start], s[i] = s[i], s[start]
        #             backtrack(i+1)
        #             s[start], s[i] = s[i], s[start]
                    
        # s = list(s)
        # s_permutation = []
        # backtrack(0) # Time Complexity: O(s*s!)
        # # Loop through result to check each permutation is in b or not
        # result: list[list[int]] = []
        # for i in range(len(s_permutation)): # Time Complexity: O(s!)
        #     permutation = ''.join(s_permutation[i])
        #     if permutation in b: # Time Complexity: O(b) => O(s!*b)
        #         for j in range(len(b)):
        #             if b[j] == permutation[0] and len(b) - j >= len(permutation):
        #                 tempArray: list[int] = []
        #                 flag: bool = True
        #                 for k, c in enumerate(permutation): # Time Complexity: O(k) => O(s!*b*k)
        #                     if c == b[j+k]:
        #                         tempArray.append(j+k)
        #                     else:
        #                         flag = False
        #                 if flag == True:
        #                     result.append(tempArray)
        # return None

        # Hash tables and sliding window
        len_s: int = len(s)
        len_b: int = len(b)
        
        s_map: dict() = Counter(s)
        window_map: dict() = Counter()
        result: list[list[int]] = []
        for i in range(len_b):
            window_map[b[i]] += 1
            
            if i >= len_s:
                if window_map[b[i - len_s]] == 1:
                    del(window_map[b[i - len_s]])
                else:
                    window_map[b[i - len_s]] -= 1

            if window_map == s_map:
                start_index: int = i - len_s + 1
                result.append(list(range(start_index, i + 1)))
                
        return result
       
    # https://leetcode.com/problems/permutation-in-string/ 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len_s1: int = len(s1)
        # len_s2: int = len(s2)

        # s1_map: dict() = Counter(s1)
        # window_sliding: dict() = Counter()

        # for i in range(len_s2):
        #     window_sliding[s2[i]] += 1

        #     if i >= len_s1:
        #         if window_sliding[s2[i - len_s1]] == 1:
        #             del(window_sliding[s2[i - len_s1]])
        #         else:
        #             window_sliding[s2[i - len_s1]] -= 1

        #     if window_sliding == s1_map:
        #         return True

        # return False
        
        # Alphabet position
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        counts1 = [0] * 26
        counts2 = [0] * 26

        for character in s1: # Time Complexity: O(s1)
            counts1[ord(character)-ord('a')] += 1 

        for i in range(len2): # Time Complexity: O(s2)
            counts2[ord(s2[i])-ord('a')] += 1
            if i >= len1:
                counts2[ord(s2[i-len1])-ord('a')] -= 1
            if counts1 == counts2:
                return True
        return False

        
if __name__ == "__main__":
    s = Solution()
    
    assert s.permute_string("ab", "cabdba") == [[1,2],[4,5]]
    assert s.permute_string("a", "cabdba") == [[1],[5]]
    assert s.permute_string("abc", "cabdbacdefabhcba") == [[0,1,2],[4,5,6],[13,14,15]]
    
    assert s.checkInclusion("ab", "cabdba") == True
    assert s.checkInclusion("a", "cabdba") == True
    assert s.checkInclusion("abc", "cabdbacdefabhcba") == True
    assert s.checkInclusion("abc", "caefb") == False
    assert s.checkInclusion("abc", "becaefb") == False