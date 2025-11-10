"""
Number of Permutations with DI Sequence
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def numPermsDISequence(S: str):
    MOD = 10**9 + 7
    n = len(S)
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if S[i-1] == 'D':
                for k in range(j, i):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
            else:
                for k in range(j):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    return sum(dp[n][j] for j in range(n+1)) % MOD
