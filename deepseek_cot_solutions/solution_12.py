"""
Problem 12: Exchange Sort

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Strategy: Chain-of-Thought (CoT)
Status: PASSED
Pass Rate: 3/3

Problem Description:
    Given a sequence (length <= 1000) of 3 different key values (7, 8, 9),
    find the minimum number of exchange operations to make the sequence sorted.
    One operation is switching 2 key values.

    Example:
        Input: [9, 9, 7, 7, 8, 8]
        Output: 4
"""

def exchange_sort(sequence):
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

