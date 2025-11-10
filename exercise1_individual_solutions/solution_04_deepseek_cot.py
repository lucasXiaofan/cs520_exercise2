"""
Unhappy Friends
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]):
    pair_map = {}
    for x, y in pairs:
        pair_map[x] = y
        pair_map[y] = x
    unhappy = set()
    for x in range(n):
        y = pair_map[x]
        for u in preferences[x]:
            if u == y:
                break
            v = pair_map[u]
            if preferences[u].index(x) < preferences[u].index(v):
                unhappy.add(x)
                break
    return len(unhappy)
