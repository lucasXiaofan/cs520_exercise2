"""
Contains Cycle in Grid
Variant: gemini_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def containsCycle(grid: List[List[str]]):
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
