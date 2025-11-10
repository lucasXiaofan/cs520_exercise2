"""Solutions for problem_1 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def maxSizeSlices_deepseek_cot(self, slices: List[int]) -> int:
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


# ========== DEEPSEEK_SELF_PLANNING ==========

from typing import List

def maxSizeSlices_deepseek_self_planning(slices: List[int]) -> int:
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


# ========== GEMINI_SELF_PLANNING ==========

class Solution:
    def maxSizeSlices_gemini_self_planning(self, slices: List[int]) -> int:
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


