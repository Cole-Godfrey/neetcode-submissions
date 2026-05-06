class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = r // 2
        row = None
        while l <= r:
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                row = m
                break
            m = (l + r) // 2
        if row is None:
            return False
        l = 0
        r = len(matrix[row]) - 1
        m = r // 2
        while l <= r:
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
            m = (l + r) // 2
        return False
        
            
            

                