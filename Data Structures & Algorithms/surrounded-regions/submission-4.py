class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        #multi source bfs from border O's, flipping each neighbor O to a T
        q = deque()
        #Seed the q with border O's
        for c in range(COLS):
            if board[0][c] == 'O':
                board[0][c] = 'T'
                q.append((0, c))
            if board[ROWS - 1][c] == 'O':
                board[ROWS - 1][c] = 'T'
                q.append((ROWS - 1, c))
        for r in range(ROWS):
            if board[r][0] == 'O':
                board[r][0] = 'T'
                q.append((r, 0))
            if board[r][COLS - 1] == 'O':
                board[r][COLS - 1] = 'T'
                q.append((r, COLS - 1))
        #Multi source bfs
        while q:
            r, c = q.popleft() # Popping an T connected to the border
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    board[nr][nc] == 'O'
                ):
                    board[nr][nc] = 'T'
                    q.append((nr, nc))
        #O(n*m) iteration thru board, flipping remaining O's to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #O(n*m) iteration flipping T's back to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'