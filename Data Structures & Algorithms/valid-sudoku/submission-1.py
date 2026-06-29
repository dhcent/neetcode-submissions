class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_col = [[set() for _ in range(9)] for _ in range(2)]
        box = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in row_col[0][row] or num in row_col[1][col] or num in box[row // 3][col // 3]:
                    return False
                row_col[0][row].add(num)
                row_col[1][col].add(num)
                box[row//3][col//3].add(num)
        return True

