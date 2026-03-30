class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                else:
                    key_row = (board[row][col], "row", row)
                    key_col = (board[row][col], "col", col)
                    key_coordinate = (board[row][col], "box", row//3, col//3)
                    if key_row in seen or key_col in seen or key_coordinate in seen:
                        return False
                    seen.add(key_row)
                    seen.add(key_col)
                    seen.add(key_coordinate)
        return True

