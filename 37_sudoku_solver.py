class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, num):
            if num in board[row]:
                return False
            for r in range(9):
                if board[r][col] == num:
                    return False
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] == num:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if is_valid(r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        backtrack()
