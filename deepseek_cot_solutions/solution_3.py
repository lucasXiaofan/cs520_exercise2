"""
Problem 3: Number of Times All Blue

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 1/1

Problem Description:
    There is a room with n bulbs numbered 1 to n. At moment k, we turn on light[k].
    A bulb changes color to blue only if it is on and all previous bulbs are turned on.

    Return the number of moments in which all turned on bulbs are blue.

    Example:
        Input: light = [2,1,3,5,4]
        Output: 3
"""

from typing import List

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_bulb = 0
        count = 0
        for i, bulb in enumerate(light):
            max_bulb = max(max_bulb, bulb)
            if max_bulb == i + 1:
                count += 1
        return count
