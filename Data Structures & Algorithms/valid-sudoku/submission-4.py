class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #return true if every row, col, 3 x 3 subgrid no duplicates

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (
                    val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True