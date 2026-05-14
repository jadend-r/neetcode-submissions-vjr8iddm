class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                #save topLeft
                topLeft = matrix[top][l + i]
                #put bottomLeft in topLeft
                matrix[top][l + i] = matrix[bottom - i][l]
                #put bottomRight in bottomLeft
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #put topRight in bottomRight
                matrix[bottom][r - i] = matrix[top + i][r]
                #put topLeft in topRight
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1