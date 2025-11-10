"""
Longest Common Subsequence
Variant: gemini_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def longestCommonSubsequence(nums: List[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for n in nums:
        if (n - 1) not in num_set:
            current_num = n
            current_streak = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
