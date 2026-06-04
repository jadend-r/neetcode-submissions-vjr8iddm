class Solution:
    def __init__(self):
        self.wasSet = set()

    def setDirection(self, r, c, direction, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        print("SET DIR CALLED")
        if (
            r < 0 or r >= ROWS or
            c < 0 or c >= COLS 
        ):
            return
        #print(f"setting {r},{c}", r, c)
        if matrix[r][c] != 0:
            matrix[r][c] = 0
            print("adding",r,c)
            self.wasSet.add((r, c))
        dr, dc = direction
        nr, nc = r + dr, c + dc
        self.setDirection(nr, nc, direction, matrix)
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        #iterate thru the grid, for every 0, dfs in each discrete direction
        for r in range(ROWS):
            print(r)
            for c in range(COLS):

                print("col", c, matrix[r][c], (r,c) not in self.wasSet)
                if matrix[r][c] == 0 and ((r, c) not in self.wasSet):
                    print("yes")
                    for direction in directions:
                        #print("swetting dir", direction, "origin", r, ",", c)
                        self.setDirection(r, c, direction, matrix)
                 
                
        