"""Solutions for problem_12 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def minimumTotal_deepseek_cot(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


# ========== DEEPSEEK_SELF_PLANNING ==========

def minimumTotal_deepseek_self_planning(self, triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    return triangle[0][0]


# ========== GEMINI_SELF_PLANNING ==========

def minimumTotal_gemini_self_planning(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = triangle

    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i][j] + dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j] + min(dp[i-1][j-1], dp[i-1][j])

    return min(dp[n-1])

