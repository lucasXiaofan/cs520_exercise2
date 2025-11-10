"""
Number of Times All Blue
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def numTimesAllBlue(light: List[int]):
    max_bulb = 0
    count = 0
    for i, bulb in enumerate(light):
        max_bulb = max(max_bulb, bulb)
        if max_bulb == i + 1:
            count += 1
    return count
