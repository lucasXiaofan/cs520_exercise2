# solution.py
from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        
        def helper(arr):
            m = len(arr)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if i == 1:
                        dp[i][j] = arr[0]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + arr[i-1])
            return dp[m][n]
        
        return max(helper(slices[1:]), helper(slices[:-1]))
    
    # def minSwaps(self, grid: List[List[int]]) -> int:
    #     """Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
    #     A grid is said to be valid if all the cells above the main diagonal are zeros.
    #     Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
    #     """
    #     n = len(grid)
    #     # For each row, find the number of trailing zeros (rightmost ones)
    #     # For grid to be valid, row i must have >= (n - 1 - i) trailing zeros
    #     # We represent the requirement for each row
    #     required = [n - 1 - i for i in range(n)]
    #     # For each row, count trailing zeros
    #     counts = []
    #     for row in grid:
    #         count = 0
    #         for j in range(len(row) - 1, -1, -1):
    #             if row[j] == 0:
    #                 count += 1
    #             else:
    #                 break
    #         counts.append(count)
        
    #     swaps = 0
        
    #     for i in range(n):
    #         # Find the first row that satisfies the requirement for current position i
    #         found = -1
    #         for j in range(i, n):
    #             if counts[j] >= required[i]:
    #                 found = j
    #                 break
    #         if found == -1:
    #             return -1
    #         # Swap rows to bring the found row to position i
    #         for j in range(found, i, -1):
    #             counts[j], counts[j - 1] = counts[j - 1], counts[j]
    #             swaps += 1
    #     return swaps
    # def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    #     pair_map = {}
    #     for x, y in pairs:
    #         pair_map[x] = y
    #         pair_map[y] = x
        
    #     unhappy = set()
        
    #     for x in range(n):
    #         y = pair_map[x]
    #         for u in preferences[x]:
    #             if u == y:
    #                 break
    #             v = pair_map[u]
    #             if preferences[u].index(x) < preferences[u].index(v):
    #                 unhappy.add(x)
    #                 break
        
    #     return len(unhappy)