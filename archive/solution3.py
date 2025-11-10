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