"""Solutions for problem_8 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

class Solution:
    def maxValueAfterReverse_deepseek_cot(self, nums: List[int]) -> int:
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


# ========== DEEPSEEK_SELF_PLANNING ==========

from typing import List

def maxValueAfterReverse_deepseek_self_planning(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    
    # Calculate the original value
    original_value = sum(abs(nums[i] - nums[i+1]) for i in range(n-1))
    
    # Initialize variables to track the maximum gain
    max_gain = 0
    
    # Calculate the gain from reversing the entire array
    gain = abs(nums[0] - nums[-1]) - abs(nums[0] - nums[1]) - abs(nums[-2] - nums[-1])
    max_gain = max(max_gain, gain)
    
    # Calculate the gain from reversing subarrays
    for i in range(1, n-1):
        # Gain from reversing from the start to i
        gain = abs(nums[0] - nums[i+1]) - abs(nums[i] - nums[i+1])
        max_gain = max(max_gain, gain)
        
        # Gain from reversing from i to the end
        gain = abs(nums[i-1] - nums[-1]) - abs(nums[i-1] - nums[i])
        max_gain = max(max_gain, gain)
    
    # Calculate the gain from reversing subarrays in the middle
    # We need to find the maximum of (nums[i] - nums[j]) and (nums[j] - nums[i]) for all i < j
    # To optimize, we can precompute the maximum and minimum values of nums[i] + nums[j] and nums[i] - nums[j]
    max1 = -float('inf')
    min1 = float('inf')
    max2 = -float('inf')
    min2 = float('inf')
    
    for i in range(n-1):
        max1 = max(max1, nums[i] + nums[i+1])
        min1 = min(min1, nums[i] + nums[i+1])
        max2 = max(max2, nums[i] - nums[i+1])
        min2 = min(min2, nums[i] - nums[i+1])
    
    # Calculate the maximum gain from the middle subarrays
    max_gain = max(max_gain, max1 - min1, max2 - min2)
    
    # Compute the final value
    final_value = original_value + max_gain
    
    return final_value


# ========== GEMINI_SELF_PLANNING ==========

class Solution:
    def maxValueAfterReverse_gemini_self_planning(self, nums: List[int]) -> int:
        n = len(nums)
        initial_value = 0
        for i in range(n - 1):
            initial_value += abs(nums[i] - nums[i + 1])

        max_value = initial_value

        for i in range(n):
            for j in range(i, n):
                new_value = 0
                
                # Calculate value before reversed subarray
                for k in range(0, i - 1):
                    new_value += abs(nums[k] - nums[k + 1])

                # Calculate value within reversed subarray
                reversed_subarray = nums[i:j+1]
                reversed_subarray.reverse()

                if i > 0:
                    new_value += abs(nums[i-1] - reversed_subarray[0])
                
                for k in range(len(reversed_subarray) - 1):
                    new_value += abs(reversed_subarray[k] - reversed_subarray[k+1])

                # Calculate value after reversed subarray
                if j < n - 1:
                    new_value += abs(reversed_subarray[-1] - nums[j+1])

                for k in range(j + 1, n - 1):
                    new_value += abs(nums[k] - nums[k + 1])

                max_value = max(max_value, new_value)

        return max_value

