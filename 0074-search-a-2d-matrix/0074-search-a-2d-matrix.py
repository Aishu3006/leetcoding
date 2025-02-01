class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top<=bottom:
            row = top + (bottom - top)//2

            if target<matrix[row][0]:
                bottom = row - 1
            elif target>matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if top>bottom:
            return False
        
        l = 0
        r = len(matrix[0])-1

        while l<=r:
            m = l + (r-l)//2

            if target>matrix[row][m]:
                l = m + 1
            elif target<matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
        
        
        
                