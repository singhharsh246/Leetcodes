"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


"""



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            data = list(j for j in board[i] if j != ".")
            if len(data) != len(set(data)):
                return (False)

            data1 = list(item[i] for item in board)
            data = list(k for k in data1 if k != ".")

            if len(data) != len(set(data)):
                return False

        for m in range(0, 7, 3):
            for n in range(0, 7, 3):
                data1 = list(kk[n:n+3] for kk in board[m:m+3])
                data = list(ite for sublist in data1 for ite in sublist if ite != ".")
                if len(data) != len(set(data)):
                    return False
        return True