"""
Number of Times All Blue
Variant: gemini_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def numTimesAllBlue(light: List[int]) -> int:
    rightmost = 0
    count = 0
    for i in range(len(light)):
        rightmost = max(rightmost, light[i])
        if rightmost == i + 1:
            count += 1
    return count
