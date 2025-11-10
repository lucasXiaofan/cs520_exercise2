"""
Maximum Pizza Slices
Variant: gemini_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def maxSizeSlices(slices: List[int]):
    n = len(slices) // 3

    def solve(arr):
        m = len(arr)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0

        for j in range(1, n + 1):
            dp[0][j] = float('-inf')

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], arr[i - 1] + dp[i - 2][j - 1] if i > 1 else arr[i-1])

        return dp[m][n]

    return max(solve(slices[:-1]), solve(slices[1:]))
