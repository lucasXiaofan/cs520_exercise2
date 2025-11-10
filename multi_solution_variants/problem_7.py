"""Solutions for problem_7 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def numPermsDISequence_deepseek_cot(self, S: str) -> int:
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


# ========== DEEPSEEK_SELF_PLANNING ==========

def numPermsDISequence_deepseek_self_planning(S: str) -> int:
    MOD = 10**9 + 7
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            if S[i - 1] == 'I':
                for k in range(j):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
            else:
                for k in range(j, i):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    return sum(dp[n]) % MOD


# ========== GEMINI_SELF_PLANNING ==========

class Solution:
    def numPermsDISequence_gemini_self_planning(self, S: str) -> int:
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7

        for i in range(1, n + 1):
            for j in range(i + 1):
                if S[i - 1] == 'I':
                    for k in range(j):
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod
                elif S[i - 1] == 'D':
                    for k in range(j, i):
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod

        result = 0
        for j in range(n + 1):
            result = (result + dp[n][j]) % mod

        return result


