class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        l = 0
        r = 1
        substrChars = set()
        substrChars.add(s[l])
        while r < len(s):
            while s[r] in substrChars:
                # substring has duplicate
                substrChars.remove(s[l])
                l += 1
            # update max substring
            res = max(r - l + 1, res)
            substrChars.add(s[r])
            r += 1
        return res

