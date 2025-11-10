"""
Problem 14: Longest Consecutive Sequence

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 1/1

Problem Description:
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    Your algorithm should run in O(n) complexity.

    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: Longest consecutive sequence is [1, 2, 3, 4], length is 4
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest = max(longest, current_streak)
        return longest
