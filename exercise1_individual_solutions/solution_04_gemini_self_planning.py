"""
Unhappy Friends
Variant: gemini_self_planning
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

    unhappy_friends = set()

    for x in range(n):
        y = pair_map[x]
        for u in preferences[x]:
            if u == y:
                break
            v = pair_map[u]
            if self.prefers(u, x, v, preferences):
                unhappy_friends.add(x)
                unhappy_friends.add(u)

    return len(unhappy_friends)

def unhappyFriends(u: int, x: int, v: int, preferences: List[List[int]]):
    for friend in preferences[u]:
        if friend == x:
            return True
        if friend == v:
            return False
    return False
