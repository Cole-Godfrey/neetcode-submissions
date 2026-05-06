class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            print("Needed: ", needed)
            print("Current num", nums[i])
            if needed in hs:
                return [hs[needed], i]
            hs[nums[i]] = i
