"""
Minimum Swaps to Make Grid Valid
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def minSwaps(grid: List[List[int]]):
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
        required = n - i - 1
        found = False
        for j in range(i, n):
            if trailing_zeros[j] >= required:
                found = True
                swaps += j - i
                trailing_zeros[i+1:j+1] = trailing_zeros[i:j]
                trailing_zeros[i] = trailing_zeros[j]
                break
        if not found:
            return -1
    return swaps
