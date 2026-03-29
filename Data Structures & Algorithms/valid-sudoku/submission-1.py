class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #return true if every row, col, 3 x 3 subgrid no duplicates

        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        squares = collections.defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                elif val in cols[c]:
                    return False
                elif val in squares[(r // 3, c // 3)]:
                    return False

                rows[r].append(val)
                cols[c].append(val)
                squares[(r // 3, c // 3)].append(val)

        return True