"""
Problem 13: Minimum Path Sum in Triangle

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 2/2

Problem Description:
    Given a triangle, find the minimum path sum from top to bottom.
    Each step you may move to adjacent numbers on the row below.

    Example:
        Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
        Output: 11 (2 + 3 + 5 + 1 = 11)
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
