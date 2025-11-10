"""Solutions for problem_13 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_SELF_PLANNING ==========

def longestConsecutive_deepseek_self_planning(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# ========== DEEPSEEK_COT ==========

class Solution:
    def longestConsecutive_deepseek_cot(self, nums: List[int]) -> int:
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


# ========== GEMINI_SELF_PLANNING ==========

def longestConsecutive_gemini_self_planning(nums: List[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for n in nums:
        if (n - 1) not in num_set:
            current_num = n
            current_streak = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

