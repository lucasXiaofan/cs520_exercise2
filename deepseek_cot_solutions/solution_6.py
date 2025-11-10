"""
Problem 6: String Mix

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 3/3

Problem Description:
    Given two strings s1 and s2, visualize how different they are by counting lowercase letters.
    Only consider letters where maximum occurrences > 1.

    Return formatted string showing differences sorted by length then lexicographically.

    Example:
        s1 = "my&friend&Paul has heavy hats! &"
        s2 = "my friend John has many many friends &"
        mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
"""

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
