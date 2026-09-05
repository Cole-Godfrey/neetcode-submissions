class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        counter = defaultdict(int)
        maxCount = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            maxCount = max(maxCount, counter[s[r]])
            windowLen = r - l + 1
            if windowLen - maxCount <= k:
                res = max(windowLen, res)
            else:
                counter[s[l]] -= 1
                l += 1
        return res