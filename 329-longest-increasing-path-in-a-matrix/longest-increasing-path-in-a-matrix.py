class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_length = 0
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def getLongestIncreasingPath(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            best = 1
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + getLongestIncreasingPath(ni, nj))

            memo[i][j] = best
            return memo[i][j]
        
        for r in range(m):
            for c in range(n):
                max_length = max(max_length, getLongestIncreasingPath(r, c))
        
        return max_length