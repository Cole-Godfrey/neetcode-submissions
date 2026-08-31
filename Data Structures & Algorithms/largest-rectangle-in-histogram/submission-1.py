class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # idx, height
        for i in range(len(heights)):
            start_idx = i
            while stack and heights[i] < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                max_area = max(area, max_area)
                start_idx = idx
            stack.append([start_idx, heights[i]])
        for idx, height in stack:
            area = (len(heights) - idx) * height
            max_area = max(area, max_area)
        return max_area

