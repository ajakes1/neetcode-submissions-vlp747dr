from collections import defaultdict


def coord_to_square(row, col) -> tuple[int,int]:
    # return coords of square start
    return (row // 3, col //3)

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                square = coord_to_square(i, j)
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in squares[square]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[square].add(board[i][j])
        return True

