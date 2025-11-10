"""
Problem 11: Longest Common Subsequence

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: FAILED
Pass Rate: 0/1

Problem Description:
    Given two strings text1 and text2, return the length of their longest common subsequence.
    A subsequence is generated from the original string with some characters deleted
    without changing the relative order.

    Example:
        Input: text1 = "abcde", text2 = "ace"
        Output: 3 (The LCS is "ace" with length 3)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
