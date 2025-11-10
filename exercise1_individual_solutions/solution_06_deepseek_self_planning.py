"""
Mix Strings
Variant: deepseek_self_planning
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def mix(s1, s2):
    from collections import defaultdict

    # Count frequencies of lowercase letters in s1 and s2
    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for char in s1:
        if char.islower():
            count1[char] += 1

    for char in s2:
        if char.islower():
            count2[char] += 1

    # Determine the maximum frequency for each letter
    max_counts = {}
    for char in set(count1.keys()).union(set(count2.keys())):
        max_count = max(count1.get(char, 0), count2.get(char, 0))
        if max_count > 1:
            max_counts[char] = max_count

    # Determine the source of the maximum frequency
    result = []
    for char, max_count in max_counts.items():
        if count1.get(char, 0) > count2.get(char, 0):
            prefix = '1:'
        elif count2.get(char, 0) > count1.get(char, 0):
            prefix = '2:'
        else:
            prefix = '=:'
        result.append(f"{prefix}{char * max_count}")

    # Sort the result
    result.sort(key=lambda x: (-len(x), x))

    # Join the result with '/' and return
    return '/'.join(result)
