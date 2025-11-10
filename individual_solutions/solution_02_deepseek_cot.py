"""
Maximum Pizza Slices
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def maxSizeSlices(slices: List[int]):
    def linear_max(s):
        n = len(s)
        m = (n + 1) // 3
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1:
                    dp[i][j] = s[0]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + s[i-1])
        return dp[n][m]
        
    case1 = linear_max(slices[:-1])
    case2 = linear_max(slices[1:])
    return max(case1, case2)
