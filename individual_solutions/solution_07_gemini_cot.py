"""
Contains Cycle in Grid
Variant: gemini_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def containsCycle(grid: List[List[str]]):
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
