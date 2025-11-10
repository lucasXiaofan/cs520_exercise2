"""
Unhappy Friends
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

from typing import List

def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    # Step 1: Initialize data structures
    pair_map = {}
    pref_rank = {}

    # Step 2: Populate pair_map
    for x, y in pairs:
        pair_map[x] = y
        pair_map[y] = x

    # Step 3: Populate pref_rank
    for i in range(n):
        pref_rank[i] = {}
        for idx, friend in enumerate(preferences[i]):
            pref_rank[i][friend] = idx

    # Step 4: Identify unhappy friends
    unhappy = set()
    for x in range(n):
        y = pair_map[x]
        for u in preferences[x]:
            if u == y:
                break
            v = pair_map[u]
            if pref_rank[u][x] < pref_rank[u][v]:
                unhappy.add(x)
                break

    # Step 5: Return the count of unhappy friends
    return len(unhappy)
