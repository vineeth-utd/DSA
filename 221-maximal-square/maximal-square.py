class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def getMaxSide(i, j):
            if i >= m or j >= n:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if matrix[i][j] == "0":
                memo[(i,j)] = 0
                return 0
            
            memo[(i,j)] = 1 + min(
                getMaxSide(i, j+1),
                getMaxSide(i+1, j+1),
                getMaxSide(i+1, j)
            )
            return memo[(i,j)]
        
        max_side = 0
        for i in range(m):
            for j in range(n):
                max_side = max(max_side, getMaxSide(i, j))

        return max_side * max_side