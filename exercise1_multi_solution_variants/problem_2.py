"""Solutions for problem_2 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def numTimesAllBlue_deepseek_cot(self, light: List[int]) -> int:
        max_bulb = 0
        count = 0
        for i, bulb in enumerate(light):
            max_bulb = max(max_bulb, bulb)
            if max_bulb == i + 1:
                count += 1
        return count


# ========== DEEPSEEK_SELF_PLANNING ==========

def numTimesAllBlue_deepseek_self_planning(self, light: List[int]) -> int:
    max_bulb = 0
    count = 0
    for k in range(len(light)):
        max_bulb = max(max_bulb, light[k])
        if max_bulb == k + 1:
            count += 1
    return count


# ========== GEMINI_SELF_PLANNING ==========

def numTimesAllBlue_gemini_self_planning(light: List[int]) -> int:
    rightmost = 0
    count = 0
    for i in range(len(light)):
        rightmost = max(rightmost, light[i])
        if rightmost == i + 1:
            count += 1
    return count

