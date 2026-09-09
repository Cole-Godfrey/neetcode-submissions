class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        matches = 0
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        for c in s1:
            s1Freq[ord(c) - ord("a")] += 1
        for c in s2[l:r + 1]:
            s2Freq[ord(c) - ord("a")] += 1
        for i in range(26):
            if s1Freq[i] == s2Freq[i]:
                matches += 1
        while r < len(s2) - 1:
            if matches == 26:
                return True
            idx = ord(s2[l]) - ord("a")
            s2Freq[idx] -= 1
            if s1Freq[idx] == s2Freq[idx]:
                matches += 1
            elif s1Freq[idx] - 1 == s2Freq[idx]:
                matches -= 1
            l += 1

            r += 1
            idx = ord(s2[r]) - ord("a")
            s2Freq[idx] += 1
            if s1Freq[idx] == s2Freq[idx]:
                matches += 1
            elif s1Freq[idx] + 1 == s2Freq[idx]:
                matches -= 1

        return matches == 26