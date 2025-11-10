"""
Minimum Swaps to Make Grid Valid
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

from typing import List

def minSwaps(grid: List[List[int]]) -> int:
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
