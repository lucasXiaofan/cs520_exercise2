"""
Problem 7: Contains Cycle in Grid

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: FAILED
Pass Rate: 0/1

Problem Description:
    Given a 2D array of characters, find if there exists any cycle of the same value.
    A cycle is a path of length >= 4 that starts and ends at the same cell.
    You can move to adjacent cells (up/down/left/right) with the same value.
    Cannot move to the cell visited in the last move.

    Example:
        Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
        Output: true
"""

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, pi, pj):
            if visited[i][j]:
                return True
            visited[i][j] = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j] and (ni != pi or nj != pj):
                    if dfs(ni, nj, i, j):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True
        return False
