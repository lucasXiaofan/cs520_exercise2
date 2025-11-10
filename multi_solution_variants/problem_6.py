"""Solutions for problem_6 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_SELF_PLANNING ==========

from typing import List

def containsCycle_deepseek_self_planning(grid: List[List[str]]) -> bool:
    if not grid or not grid[0]:
        return False
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r, c, pr, pc, char):
        if visited[r][c]:
            return True
        visited[r][c] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char and not (nr == pr and nc == pc):
                if dfs(nr, nc, r, c, char):
                    return True
        return False
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
    return False


# ========== DEEPSEEK_COT ==========

class Solution:
    def containsCycle_deepseek_cot(self, grid: List[List[str]]) -> bool:
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


# ========== GEMINI_COT ==========

class Solution:
    def containsCycle_gemini_cot(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col, parent_row, parent_col, start_char):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != start_char:
                return False
            
            if visited[row][col]:
                return True

            visited[row][col] = True

            # Explore neighbors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and (new_row != parent_row or new_col != parent_col) and grid[new_row][new_col] == start_char:
                    if dfs(new_row, new_col, row, col, start_char):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False


# ========== GEMINI_SELF_PLANNING ==========

class Solution:
    def containsCycle_gemini_self_planning(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(row, col, parent_row, parent_col, start_row, start_col):
            if (row, col) in visited:
                return True

            visited.add((row, col))

            # Explore neighbors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == grid[row][col] and (new_row, new_col) != (parent_row, parent_col):
                    if dfs(new_row, new_col, row, col, start_row, start_col):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1, i, j):
                        return True

        return False

