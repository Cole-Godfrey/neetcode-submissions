class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if (maxL <= maxR):
                l += 1
                maxL = max(maxL, height[l])
                total  += max(maxL - height[l], 0)
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += max(maxR - height[r], 0)
        return total
            


