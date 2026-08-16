class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        lcs = 0
        for num in numbers:
            if num - 1 not in numbers:
                # start of a seq
                seq = 1
                cnum = num + 1
                while cnum in numbers:
                    seq += 1
                    cnum += 1
                if seq > lcs:
                    lcs = seq
        return lcs
