"""Solutions for problem_4 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_SELF_PLANNING ==========

from typing import List

def minSwaps_deepseek_self_planning(grid: List[List[int]]) -> int:
    n = len(grid)
    # Step 1: Calculate the required trailing zeros for each row
    required = [n - i - 1 for i in range(n)]
    
    # Step 2: Calculate the actual trailing zeros for each row
    actual = []
    for row in grid:
        count = 0
        for num in reversed(row):
            if num == 0:
                count += 1
            else:
                break
        actual.append(count)
    
    # Step 3: Match required trailing zeros with actual trailing zeros
    swaps = 0
    for i in range(n):
        # Step 4: Find the nearest row below that has at least the required trailing zeros
        j = i
        while j < n and actual[j] < required[i]:
            j += 1
        if j == n:
            return -1
        # Step 5: Swap rows and count the number of swaps
        while j > i:
            actual[j], actual[j - 1] = actual[j - 1], actual[j]
            swaps += 1
            j -= 1
    
    # Step 6: Return the total number of swaps
    return swaps


# ========== DEEPSEEK_COT ==========

class Solution:
    def minSwaps_deepseek_cot(self, grid: List[List[int]]) -> int:
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


# ========== GEMINI_SELF_PLANNING ==========

def minSwaps_gemini_self_planning(grid: List[List[int]]) -> int:
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
        required_zeros = n - 1 - i
        j = i
        while j < n and trailing_zeros[j] < required_zeros:
            j += 1

        if j == n:
            return -1

        for k in range(j, i, -1):
            trailing_zeros[k], trailing_zeros[k - 1] = trailing_zeros[k - 1], trailing_zeros[k]
            swaps += 1

    return swaps

