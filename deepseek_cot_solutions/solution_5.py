"""
Problem 5: Minimum Swaps to Validate Grid

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: FAILED
Pass Rate: 0/1

Problem Description:
    Given an n x n binary grid, swap two adjacent rows to make the grid valid.
    A grid is valid if all cells above the main diagonal are zeros.

    Return the minimum number of steps, or -1 if impossible.

    Example:
        Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
        Output: 3
"""

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        swaps = 0
        for i in range(n):
            required = n - i - 1
            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    found = True
                    swaps += j - i
                    trailing_zeros[i+1:j+1] = trailing_zeros[i:j]
                    trailing_zeros[i] = trailing_zeros[j]
                    break
            if not found:
                return -1
        return swaps
