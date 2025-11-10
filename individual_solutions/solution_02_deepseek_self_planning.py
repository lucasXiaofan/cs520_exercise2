"""
Maximum Pizza Slices
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

from typing import List

def maxSizeSlices(slices: List[int]) -> int:
    def dp_helper(arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j] = arr[i]
                else:
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i >= 1 else 0) + arr[i])
        return dp[n - 1][k]

    n = len(slices)
    k = n // 3
    case1 = dp_helper(slices[:-1], k)
    case2 = dp_helper(slices[1:], k)
    return max(case1, case2)
