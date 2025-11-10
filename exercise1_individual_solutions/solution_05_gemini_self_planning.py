"""
Minimum Swaps to Make Grid Valid
Variant: gemini_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)
    trailing_zeros = []
    for row in grid:
        count = 0
        for i in range(n - 1, -1, -1):
            if row[i] == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)

    swaps = 0
    for i in range(n):
        required_zeros = n - 1 - i
        j = i
        while j < n and trailing_zeros[j] < required_zeros:
            j += 1

        if j == n:
            return -1

        for k in range(j, i, -1):
            trailing_zeros[k], trailing_zeros[k - 1] = trailing_zeros[k - 1], trailing_zeros[k]
            swaps += 1

    return swaps
