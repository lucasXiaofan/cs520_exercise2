"""
Contains Cycle in Grid
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

from typing import List

def containsCycle(grid: List[List[str]]) -> bool:
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
