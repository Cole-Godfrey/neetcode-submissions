class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        tCounter = Counter(t)
        l = 0
        res = []
        resLen = float('infinity')
        need = len(tCounter)
        have = 0
        window = defaultdict(int)

        for r in range(len(s)):
            # add r to window
            char = s[r]
            window[char] += 1
            if char in tCounter and tCounter[char] == window[char]:
                have += 1
            # increment l until no longer good
            while have >= need:
                newLen = r - l + 1
                if have >= need and newLen < resLen:
                    # update new best substr
                    res = [l, r + 1]
                    resLen = newLen
                char = s[l]
                window[char] -= 1
                if char in tCounter and window[char] == tCounter[char] - 1:
                    have -= 1
                l += 1
        return s[res[0]:res[1]] if res else ""
            
            
            
