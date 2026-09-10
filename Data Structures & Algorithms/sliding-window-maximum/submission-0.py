class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        l = 0
        r = k
        # fill dq with initial numbers in window
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        while r < len(nums):
            # update left
            if dq[0] == l:
                dq.popleft()
            l += 1
            # update right
            r += 1
            num = nums[r - 1]
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(r - 1)
            res.append(nums[dq[0]])
        return res