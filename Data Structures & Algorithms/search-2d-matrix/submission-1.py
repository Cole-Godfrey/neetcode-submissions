class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row target could be in
        l = 0
        r = len(matrix) - 1
        m = -1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        if not (l <= r):
            return False
        # binary search on selected row
        row = m
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False