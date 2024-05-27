# You are given a binary string s (a string containing only "0" and "1"). 
# You may choose up to one "0" and flip it to a "1". 
# What is the length of the longest substring achievable that contains only "1"?

# For example, given s = "1101100111", the answer is 5. 
# If you perform the flip at index 2, the string becomes 1111100111.

class Solution:
    def longest_subarray_string_flip_one(self, my_string: str) -> int:
        # sliding window
        left = current = answer = 0
        for right in range(len(my_string)):
            if my_string[right] == "0":
                current += 1
            while current > 1:
                if my_string[left] == "0":
                    current -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer
    
        # brute force
        # sub_str: str = ""
        # answer: int = 0
        # for c in my_string:
        #     if int(c) == 1 or (int(c) == 0 and '0' not in sub_str):
        #         sub_str += c
        #     else:
        #         sub_str = ""
        #     answer = max(answer, len(sub_str))
        # return answer
    
if __name__ == "__main__":
    s = Solution()
    
    result = s.longest_subarray_string_flip_one('1')
    assert result == 1
    
    result = s.longest_subarray_string_flip_one('01')
    assert result == 2
    
    result = s.longest_subarray_string_flip_one('1101100111')
    assert result == 5
    
    result = s.longest_subarray_string_flip_one('110110011111')
    assert result == 6