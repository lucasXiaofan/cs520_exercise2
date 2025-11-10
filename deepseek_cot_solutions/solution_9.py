"""
Problem 9: Maximum Value After Reverse

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 1/1

Problem Description:
    Given an integer array nums, the value is defined as sum of |nums[i]-nums[i+1]| for all i.
    You can select any subarray and reverse it (only once).

    Find maximum possible value of the final array.

    Example:
        Input: nums = [2,3,1,5,4]
        Output: 10
"""

from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        original_value = sum(abs(nums[i] - nums[i+1]) for i in range(len(nums)-1))
        max_gain = 0
        for i in range(len(nums)-1):
            if i > 0:
                gain = abs(nums[i+1] - nums[0]) - abs(nums[i] - nums[0])
                max_gain = max(max_gain, gain)
            if i < len(nums)-1:
                gain = abs(nums[i] - nums[-1]) - abs(nums[i+1] - nums[-1])
                max_gain = max(max_gain, gain)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i > 0:
                    gain = abs(nums[j] - nums[i-1]) - abs(nums[i] - nums[i-1])
                    max_gain = max(max_gain, gain)
                if j < len(nums)-1:
                    gain = abs(nums[i] - nums[j+1]) - abs(nums[j] - nums[j+1])
                    max_gain = max(max_gain, gain)
        return original_value + max_gain
