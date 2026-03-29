class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while t <= b:
            m = (t + b) // 2
            if target in matrix[m]:
                # binary seach in matrix[m]
                while l <= r:
                    m2 = (l + r) // 2
                    if matrix[m][m2] == target:
                        return True
                    elif matrix[m][m2] < target:
                        l = m2 + 1
                    else:
                        r = m2 - 1
            elif target > matrix[m][-1]:
                t = m + 1
            else: 
                b = m - 1

        return False