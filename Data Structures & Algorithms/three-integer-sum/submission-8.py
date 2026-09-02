class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # if we have already used this value for a, skip it
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            target = 0 - a
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # can't have duplicate, same logic for a
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
