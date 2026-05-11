class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        hashmap = {}
        for num in nums:
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[num] = i
            i += 1