"""
Least Operators to Express Target
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(i, t):
            if t == 0:
                return 0
            if i == 0:
                return t * 2 - 1
            k = t // (x ** i)
            r = t % (x ** i)
            return min(k * i + dp(i - 1, r), (k + 1) * i + dp(i - 1, x ** i - r))
        
        if x == target:
            return 0
        i = 0
        while x ** i <= target:
            i += 1
        return dp(i - 1, target) - 1
