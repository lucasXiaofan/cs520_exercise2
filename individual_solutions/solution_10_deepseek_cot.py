"""
Least Operators to Express Target
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def leastOpsExpressTarget(x: int, target: int):
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def dp(i, t):
        if t == 0:
            return 0
        if t == 1:
            return 1 if i == 0 else i
        if i >= 39:
            return float('inf')
        if x > t:
            return min(t * 2 - 1, (x - t) * 2)
        k = 0
        while x ** (k + 1) <= t:
            k += 1
        res = k + dp(i + 1, t - x ** k)
        if x ** (k + 1) - t < t:
            res = min(res, k + 1 + dp(i + 1, x ** (k + 1) - t))
        return res
    return dp(0, target)
