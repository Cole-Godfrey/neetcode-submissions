class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[m] >= nums[l]:
                # in left subarray
                if target < nums[m]: 
                    if target < nums[l]:
                        # look in right subarray
                        l = m + 1
                    else:
                        # look in left subarray
                        r = m - 1
                else:
                    # look to right in left subarray
                    l = m + 1
            else:
                # in right subarray
                if target < nums[m]:
                    # look to the left in right subarray
                    r = m - 1
                else:
                    if target > nums[r]:
                        # look in left subarray
                        r = m - 1
                    else:
                        # look to right in right subarray
                        l = m + 1
        return -1
