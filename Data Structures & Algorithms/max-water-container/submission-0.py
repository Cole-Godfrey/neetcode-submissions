class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                height = min(heights[i], heights[j])
                length = abs(i - j)
                area = length * height
                maxArea = max(maxArea, area)
        return maxArea
