"""
Number of Times All Blue
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def numTimesAllBlue(self, light: List[int]) -> int:
    max_bulb = 0
    count = 0
    for k in range(len(light)):
        max_bulb = max(max_bulb, light[k])
        if max_bulb == k + 1:
            count += 1
    return count
