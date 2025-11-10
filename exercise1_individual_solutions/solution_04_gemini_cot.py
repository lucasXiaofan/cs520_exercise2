"""
Unhappy Friends
Variant: gemini_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]):
    pair_dict = {}
    for x, y in pairs:
        pair_dict[x] = y
        pair_dict[y] = x

    unhappy_friends = set()

    for x in range(n):
        y = pair_dict[x]
        for u in range(n):
            if u != x and u != y:
                v = pair_dict[u]
                    
                # Check if x prefers u over y
                x_prefers_u = False
                for preferred_friend in preferences[x]:
                    if preferred_friend == u:
                        x_prefers_u = True
                        break
                    if preferred_friend == y:
                        break
                    
                # Check if u prefers x over v
                u_prefers_x = False
                for preferred_friend in preferences[u]:
                    if preferred_friend == x:
                        u_prefers_x = True
                        break
                    if preferred_friend == v:
                        break

                if x_prefers_u and u_prefers_x:
                    unhappy_friends.add(x)

    return len(unhappy_friends)
