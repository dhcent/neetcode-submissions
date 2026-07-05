class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # same idea except now our "center" will be the (middle index + 1)% num rows to get col, and // num rows to get row

        L = 0
        num_rows = len(matrix)
        num_col = len(matrix[0])
        R = num_rows * num_col - 1

        while L <= R:
            center = int(L + (R - L)/2)
            col = center % num_col
            row = center // num_col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                R = center - 1
            else:
                L = center + 1
        return False
        