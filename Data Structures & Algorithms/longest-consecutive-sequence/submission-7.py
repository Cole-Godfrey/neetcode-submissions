class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums)) # convert to set than back to remove duplicates
        nums.sort()
        print(nums)
        seqlen = 1
        maxseqlen = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                seqlen += 1
            # end of seq
            else: 
                seqlen = 1
            maxseqlen = max(seqlen, maxseqlen)
        return maxseqlen
            