class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                digit = board[r][c]
                if digit == '.':
                    continue
                box = (r // 3, c // 3)
                print(r, c, box)
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    print(digit)
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
        return True