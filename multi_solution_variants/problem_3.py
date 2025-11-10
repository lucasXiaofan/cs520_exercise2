"""Solutions for problem_3 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def unhappyFriends_deepseek_cot(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
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


# ========== DEEPSEEK_SELF_PLANNING ==========

from typing import List

def unhappyFriends_deepseek_self_planning(n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
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


# ========== GEMINI_SELF_PLANNING ==========

class Solution:
    def unhappyFriends_gemini_self_planning(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
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

    def prefers(self, u: int, x: int, v: int, preferences: List[List[int]]) -> bool:
        for friend in preferences[u]:
            if friend == x:
                return True
            if friend == v:
                return False
        return False



# ========== GEMINI_COT ==========

class Solution:
    def unhappyFriends_gemini_cot(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
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

