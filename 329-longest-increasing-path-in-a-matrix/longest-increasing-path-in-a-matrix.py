class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_length = 0
        memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        def getLongestIncreasingPath(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            left = right = top = bottom = 0

            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                left = getLongestIncreasingPath(i, j-1)
            if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                bottom = getLongestIncreasingPath(i+1, j)
            if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                right = getLongestIncreasingPath(i, j+1)
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                top = getLongestIncreasingPath(i-1, j)

            memo[i][j] = 1 + max(
                left,
                bottom,
                right,
                top
            )
            return memo[i][j]
        
        for r in range(m):
            for c in range(n):
                max_length = max(max_length, getLongestIncreasingPath(r, c))
        
        return max_length