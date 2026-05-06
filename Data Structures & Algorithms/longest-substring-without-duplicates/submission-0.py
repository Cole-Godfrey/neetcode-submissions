class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_substring = 0

        while r < len(s):
            substring = s[l:r]
            # if final letter is duplicate
            if s[r] in substring:
                l += 1
            else: 
                # not duplicate, calculate len
                len_ss = len(substring) + 1
                longest_substring = max(len_ss, longest_substring)
                r += 1
            
        return longest_substring

