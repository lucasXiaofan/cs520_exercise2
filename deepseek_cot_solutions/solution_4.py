"""
Problem 4: Unhappy Friends

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: FAILED
Pass Rate: 0/1

Problem Description:
    You are given preferences for n friends (n is even). For each person, preferences[i] contains
    a sorted list of friends. Friends are divided into pairs.

    A friend x is unhappy if x is paired with y and there exists u paired with v where:
    - x prefers u over y, and
    - u prefers x over v

    Return the number of unhappy friends.

    Example:
        Input: n=4, preferences=[[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs=[[0,1],[2,3]]
        Output: 2
"""

from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
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
