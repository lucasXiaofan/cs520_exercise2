"""
Problem 8: Number of Permutations for DI Sequence

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 1/1

Problem Description:
    Given string S of length n with characters from {'D', 'I'} (decreasing/increasing).
    A valid permutation P[0]...P[n] of {0,1,...,n} satisfies:
    - If S[i] == 'D', then P[i] > P[i+1]
    - If S[i] == 'I', then P[i] < P[i+1]

    Return number of valid permutations modulo 10^9 + 7.

    Example:
        Input: "DID"
        Output: 5
"""

class Solution:
    def numPermsDISequence(self, S: str) -> int:
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
