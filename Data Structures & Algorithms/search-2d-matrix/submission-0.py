class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        while(top<=bottom):
            rowmid = (top + bottom) // 2

            if target > matrix[rowmid][columns-1]:
                top = rowmid + 1
            elif target < matrix[rowmid][0]:
                bottom = rowmid - 1
            else:
                break
        
        if not (top<=bottom):
            return False

        rowmid = (top + bottom) // 2
        l = 0
        r = columns-1

        while(l<=r):
            mid = (l + r) // 2
            if target > matrix[rowmid][mid]:
                l = mid + 1
            elif target < matrix[rowmid][mid]:
                r = mid - 1
            else:
                return True
        
        return False
