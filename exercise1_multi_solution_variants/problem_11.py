"""Solutions for problem_11 - All variants"""

# This file is auto-generated. Do not edit manually.

# ========== DEEPSEEK_COT ==========

def exchange_sort_deepseek_cot(sequence):
    sorted_seq = sorted(sequence)
    swaps = 0
    seq = sequence.copy()
    for i in range(len(seq)):
        if seq[i] != sorted_seq[i]:
            j = i + 1
            while j < len(seq) and seq[j] != sorted_seq[i]:
                j += 1
            if j < len(seq):
                seq[i], seq[j] = seq[j], seq[i]
                swaps += 1
    return swaps


# ========== DEEPSEEK_SELF_PLANNING ==========

def exchange_sort_deepseek_self_planning(sequence):
    # Count the occurrences of each value
    count_7 = sequence.count(7)
    count_8 = sequence.count(8)
    count_9 = sequence.count(9)
    
    # Define the correct positions
    correct_sequence = [7] * count_7 + [8] * count_8 + [9] * count_9
    
    # Initialize the number of swaps
    swaps = 0
    
    # Create a copy of the sequence to avoid modifying the original
    sequence_copy = sequence.copy()
    
    # Iterate through the sequence and perform swaps
    for i in range(len(sequence_copy)):
        if sequence_copy[i] != correct_sequence[i]:
            # Find the correct element to swap with
            for j in range(i + 1, len(sequence_copy)):
                if sequence_copy[j] == correct_sequence[i]:
                    # Swap the elements
                    sequence_copy[i], sequence_copy[j] = sequence_copy[j], sequence_copy[i]
                    swaps += 1
                    break
    
    return swaps


# ========== GEMINI_COT ==========

def exchange_sort_gemini_cot(sequence):
    n = len(sequence)
    sorted_sequence = sorted(sequence)
    
    count78 = 0
    count87 = 0
    count79 = 0
    count97 = 0
    count89 = 0
    count98 = 0
    
    num7 = sorted_sequence.count(7)
    num8 = sorted_sequence.count(8)
    
    for i in range(n):
        if i < num7:
            if sequence[i] == 8:
                count78 += 1
            elif sequence[i] == 9:
                count79 += 1
        elif i < num7 + num8:
            if sequence[i] == 7:
                count87 += 1
            elif sequence[i] == 9:
                count89 += 1
        else:
            if sequence[i] == 7:
                count97 += 1
            elif sequence[i] == 8:
                count98 += 1
                
    ans = max(count78, count87) + max(count79, count97) + max(count89, count98) - min(max(count79, count97), max(count89, count98))
    ans = max(count78, count87) + max(0, count79 + count89 - max(count78, count87))
    
    return ans

