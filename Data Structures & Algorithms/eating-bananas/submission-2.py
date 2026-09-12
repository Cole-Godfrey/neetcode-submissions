class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = max(piles)
        l = 1
        r = largest_pile
        res = r
        while l <= r:
            k = (l + r) // 2
            # test this k
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            if total_time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res