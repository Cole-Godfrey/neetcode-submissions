class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hashmap = Counter(s1)
        l = 0
        r = len(s1)
        while r < len(s2) + 1:
            s2Hashmap = Counter(s2[l:r])
            if s1Hashmap == s2Hashmap:
                return True
            l += 1
            r += 1
        return False