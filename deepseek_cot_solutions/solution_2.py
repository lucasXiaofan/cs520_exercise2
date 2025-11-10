"""
Problem 2: Maximum Pizza Slices

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 1/1

Problem Description:
    There is a pizza with 3n slices of varying size. You and your friends will take slices as follows:
    - You will pick any pizza slice
    - Friend Alice will pick next slice in anti-clockwise direction
    - Friend Bob will pick next slice in clockwise direction
    - Repeat until no more slices

    Return the maximum possible sum of slice sizes which you can have.

    Example:
        Input: slices = [1,2,3,4,5,6]
        Output: 10
"""

from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
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
