import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bph = max(piles)
        mid = max_bph // 2
        l = 1
        r = max_bph
        while l < r:
            num_hours = 0
            max_hours = h
            for pile in piles:
                num_hours += math.ceil(pile / mid)
            if num_hours <= max_hours:
                r = mid
            else:
                l = mid + 1

            mid = (l + r) // 2
        return l
