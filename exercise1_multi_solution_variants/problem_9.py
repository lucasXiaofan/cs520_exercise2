"""Solutions for problem_9 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def leastOpsExpressTarget_deepseek_cot(self, x: int, target: int) -> int:
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


# ========== DEEPSEEK_SELF_PLANNING ==========

from functools import lru_cache

class Solution:
    def leastOpsExpressTarget_deepseek_self_planning(self, x: int, target: int) -> int:
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

