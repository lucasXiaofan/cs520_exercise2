"""
Mix Strings
Variant: deepseek_cot
"""

from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

def mix(s1, s2):
    from collections import defaultdict
    count1 = defaultdict(int)
    count2 = defaultdict(int)
    for char in s1:
        if char.islower():
            count1[char] += 1
    for char in s2:
        if char.islower():
            count2[char] += 1
    result = []
    for char in set(count1.keys()).union(set(count2.keys())):
        max_count = max(count1.get(char, 0), count2.get(char, 0))
        if max_count > 1:
            if count1.get(char, 0) > count2.get(char, 0):
                result.append(f'1:{char * max_count}')
            elif count2.get(char, 0) > count1.get(char, 0):
                result.append(f'2:{char * max_count}')
            else:
                result.append(f'=:{char * max_count}')
    result.sort(key=lambda x: (-len(x), x))
    return '/'.join(result)
