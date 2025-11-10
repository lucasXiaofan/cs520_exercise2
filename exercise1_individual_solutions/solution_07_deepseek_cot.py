"""
Contains Cycle in Grid
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def containsCycle(grid: List[List[str]]):
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
