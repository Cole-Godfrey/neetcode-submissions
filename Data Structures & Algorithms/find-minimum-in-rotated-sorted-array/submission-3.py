class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float('infinity')
        while l <= r:
            # if in fully sorted, take min (first element)
            if nums[r] > nums[l]:
                return min(res, nums[l])
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # search right
                l = m + 1
            else:
                # search left
                r = m - 1
        return res