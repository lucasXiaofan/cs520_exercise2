"""
Test suite for all 14 APPS dataset problems
Uses pytest and pytest-cov for coverage analysis

Run tests with:
    pytest test_all_problems.py -v

Run with coverage:
    pytest test_all_problems.py -v --cov=. --cov-report=term-missing --cov-branch

Model: DeepSeek V3 (deepseek/deepseek-chat-v3)
Prompt Strategy: Chain-of-Thought (CoT)
"""

import pytest
from typing import List
import sys

# Import all solution modules from deepseek_cot_solutions folder
try:
    from deepseek_cot_solutions.solution_1 import b91decode, b91encode
except ImportError:
    b91decode = b91encode = None

try:
    from deepseek_cot_solutions.solution_2 import Solution as Solution2
except ImportError:
    Solution2 = None

try:
    from deepseek_cot_solutions.solution_3 import Solution as Solution3
except ImportError:
    Solution3 = None

try:
    from deepseek_cot_solutions.solution_4 import Solution as Solution4
except ImportError:
    Solution4 = None

try:
    from deepseek_cot_solutions.solution_5 import Solution as Solution5
except ImportError:
    Solution5 = None

try:
    from deepseek_cot_solutions.solution_6 import mix
except ImportError:
    mix = None

try:
    from deepseek_cot_solutions.solution_7 import Solution as Solution7
except ImportError:
    Solution7 = None

try:
    from deepseek_cot_solutions.solution_8 import Solution as Solution8
except ImportError:
    Solution8 = None

try:
    from deepseek_cot_solutions.solution_9 import Solution as Solution9
except ImportError:
    Solution9 = None

try:
    from deepseek_cot_solutions.solution_10 import Solution as Solution10
except ImportError:
    Solution10 = None

try:
    from deepseek_cot_solutions.solution_11 import Solution as Solution11
except ImportError:
    Solution11 = None

try:
    from deepseek_cot_solutions.solution_12 import exchange_sort
except ImportError:
    exchange_sort = None

try:
    from deepseek_cot_solutions.solution_13 import Solution as Solution12
except ImportError:
    Solution12 = None

try:
    from deepseek_cot_solutions.solution_14 import Solution as Solution13
except ImportError:
    Solution13 = None

try:
    from deepseek_cot_solutions.solution_11 import Solution as Solution14
except ImportError:
    Solution14 = None


class TestProblem1:
    """
    Problem 1: Base91 Encode/Decode

    [BasE91](http://base91.sourceforge.net/) is a method for encoding binary as ASCII characters.
    It is more efficient than Base64 and needs 91 characters to represent the encoded data.

    Create two functions that encode strings to basE91 string and decodes the other way round.

    Examples:
        b91encode('test') = 'fPNKd'
        b91decode('fPNKd') = 'test'
        b91decode('>OwJh>Io0Tv!8PE') = 'Hello World!'
        b91encode('Hello World!') = '>OwJh>Io0Tv!8PE'
    """

    def test_base91_decode_1(self):
        print("\n=== Testing Problem 1: Base91 Decode ===")
        if b91decode is None:
            pytest.skip("solution_1.py not found")
        assert b91decode(">OwJh>Io0Tv!8PE") == "Hello World!"

    def test_base91_decode_2(self):
        if b91decode is None:
            pytest.skip("solution_1.py not found")
        assert b91decode("fPNKd") == "test"


class TestProblem2:
    """
    Problem 2: Maximum Pizza Slices

    There is a pizza with 3n slices of varying size. You and your friends will take slices as follows:
    - You will pick any pizza slice
    - Friend Alice will pick next slice in anti-clockwise direction
    - Friend Bob will pick next slice in clockwise direction
    - Repeat until no more slices

    Return the maximum possible sum of slice sizes which you can have.

    Example:
        Input: slices = [1,2,3,4,5,6]
        Output: 10
    """

    def test_max_pizza_slices(self):
        print("\n=== Testing Problem 2: Maximum Pizza Slices ===")
        if Solution2 is None:
            pytest.skip("solution_2.py not found")
        solution = Solution2()
        assert solution.maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10


class TestProblem3:
    """
    Problem 3: Number of Times All Blue

    There is a room with n bulbs numbered 1 to n. At moment k, we turn on light[k].
    A bulb changes color to blue only if it is on and all previous bulbs are turned on.

    Return the number of moments in which all turned on bulbs are blue.

    Example:
        Input: light = [2,1,3,5,4]
        Output: 3
    """

    def test_num_times_all_blue(self):
        print("\n=== Testing Problem 3: Number of Times All Blue ===")
        if Solution3 is None:
            pytest.skip("solution_3.py not found")
        solution = Solution3()
        assert solution.numTimesAllBlue([2, 1, 3, 5, 4]) == 3


class TestProblem4:
    """
    Problem 4: Unhappy Friends

    You are given preferences for n friends (n is even). For each person, preferences[i] contains
    a sorted list of friends. Friends are divided into pairs.

    A friend x is unhappy if x is paired with y and there exists u paired with v where:
    - x prefers u over y, and
    - u prefers x over v

    Return the number of unhappy friends.

    Example:
        Input: n=4, preferences=[[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs=[[0,1],[2,3]]
        Output: 2
    """

    # def test_unhappy_friends(self):
    #     print("\n=== Testing Problem 4: Unhappy Friends ===")
    #     if Solution4 is None:
    #         pytest.skip("solution_4.py not found")
    #     solution = Solution4()
    #     result = solution.unhappyFriends(
    #         4,
    #         [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0], [], []],
    #         [[0, 1], [2, 3], [], []]
    #     )
    #     assert result == 2

    @pytest.mark.parametrize("n,preferences,pairs,expected", [
        (4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]], 2),
        # (2, [[1],[0]], [[1,0]], 0),
        # (4, [[1,3,2],[2,3,0],[1,3,0],[0,2,1]], [[1,3],[0,2]], 4),
    ])
    def test_unhappy_friends(self, n, preferences, pairs, expected):
        solution = Solution4()
        assert solution.unhappyFriends(n, preferences, pairs) == expected


class TestProblem5:
    """
    Problem 5: Minimum Swaps to Make Grid Valid

    Given an n x n binary grid, swap two adjacent rows to make the grid valid.
    A grid is valid if all cells above the main diagonal are zeros.

    Return the minimum number of steps, or -1 if impossible.

    Example:
        Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
        Output: 3
    """

    def test_min_swaps(self):
        print("\n=== Testing Problem 5: Minimum Swaps ===")
        if Solution5 is None:
            pytest.skip("solution_5.py not found")
        solution = Solution5()
        assert solution.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0], [], []]) == 3


class TestProblem6:
    """
    Problem 6: Mix Strings

    Given two strings s1 and s2, visualize how different they are by counting lowercase letters.
    Only consider letters where maximum occurrences > 1.

    Return formatted string showing differences sorted by length then lexicographically.

    Example:
        s1 = "my&friend&Paul has heavy hats! &"
        s2 = "my friend John has many many friends &"
        mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
    """

    def test_mix_1(self):
        print("\n=== Testing Problem 6: Mix Strings ===")
        if mix is None:
            pytest.skip("solution_6.py not found")
        result = mix("looping is fun but dangerous", "less dangerous than coding")
        assert result == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    def test_mix_2(self):
        if mix is None:
            pytest.skip("solution_6.py not found")
        result = mix("Are they here", "yes, they are here")
        assert result == "2:eeeee/2:yy/=:hh/=:rr"

    def test_mix_3(self):
        if mix is None:
            pytest.skip("solution_6.py not found")
        result = mix("Lords of the Fallen", "gamekult")
        assert result == "1:ee/1:ll/1:oo"


class TestProblem7:
    """
    Problem 7: Contains Cycle in Grid

    Given a 2D array of characters, find if there exists any cycle of the same value.
    A cycle is a path of length >= 4 that starts and ends at the same cell.
    You can move to adjacent cells (up/down/left/right) with the same value.
    Cannot move to the cell visited in the last move.

    Example:
        Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
        Output: true
    """

    def test_contains_cycle(self):
        print("\n=== Testing Problem 7: Contains Cycle ===")
        if Solution7 is None:
            pytest.skip("solution_7.py not found")
        solution = Solution7()
        grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"],[],[]]
        assert solution.containsCycle(grid) == True


class TestProblem8:
    """
    Problem 8: Number of Permutations with DI Sequence

    Given string S of length n with characters from {'D', 'I'} (decreasing/increasing).
    A valid permutation P[0]...P[n] of {0,1,...,n} satisfies:
    - If S[i] == 'D', then P[i] > P[i+1]
    - If S[i] == 'I', then P[i] < P[i+1]

    Return number of valid permutations modulo 10^9 + 7.

    Example:
        Input: "DID"
        Output: 5
    """

    def test_num_perms_di_sequence(self):
        print("\n=== Testing Problem 8: DI Sequence ===")
        if Solution8 is None:
            pytest.skip("solution_8.py not found")
        solution = Solution8()
        assert solution.numPermsDISequence("DID") == 5


class TestProblem9:
    """
    Problem 9: Maximum Value After Reverse

    Given an integer array nums, the value is defined as sum of |nums[i]-nums[i+1]| for all i.
    You can select any subarray and reverse it (only once).

    Find maximum possible value of the final array.

    Example:
        Input: nums = [2,3,1,5,4]
        Output: 10
    """

    def test_max_value_after_reverse(self):
        print("\n=== Testing Problem 9: Max Value After Reverse ===")
        if Solution9 is None:
            pytest.skip("solution_9.py not found")
        solution = Solution9()
        assert solution.maxValueAfterReverse([2, 3, 1, 5, 4]) == 10


class TestProblem10:
    """
    Problem 10: Least Operators to Express Target

    Given x and target, write an expression "x op1 x op2 x op3..." where operators are +, -, *, /.
    Follow standard order of operations (no parentheses, no unary negation).

    Return the least number of operators to equal the target.

    Example:
        Input: x = 3, target = 19
        Output: 5 (3 * 3 + 3 * 3 + 3 / 3)
    """

    def test_least_ops_express_target(self):
        print("\n=== Testing Problem 10: Least Operators ===")
        if Solution10 is None:
            pytest.skip("solution_10.py not found")
        solution = Solution10()
        assert solution.leastOpsExpressTarget(3, 19) == 5


class TestProblem11:
    """
    Problem 11: Exchange Sort

    Given a sequence (length <= 1000) of 3 different key values (7, 8, 9),
    find the minimum number of exchange operations to make the sequence sorted.
    One operation is switching 2 key values.

    Example:
        Input: [9, 9, 7, 7, 8, 8]
        Output: 4
    """
    def test_exchange_sort(self):
    # Test case 1: Already sorted sequence
        assert exchange_sort([7, 7, 8, 8, 9, 9]) == 0

        # Test case 2: Partially sorted sequence
        assert exchange_sort([7, 9, 8, 7, 8, 9]) == 2

        # Test case 3: Fully unsorted sequence
        assert exchange_sort([9, 9, 7, 7, 8, 8]) == 4

        # Test case 4: Sequence with only one type of value
        assert exchange_sort([7, 7, 7, 7]) == 0

        # Test case 5: Edge case with minimum sequence length
        assert exchange_sort([7]) == 0

        # Test case 6: Empty sequence
        assert exchange_sort([]) == 0

        # Test case 7: Sequence with all 8s
        assert exchange_sort([8, 8, 8, 8]) == 0

        # Test case 8: Sequence with all 9s
        assert exchange_sort([9, 9, 9, 9]) == 0

        # Test case 9: Mixed sequence with varying lengths
        assert exchange_sort([7, 8, 9, 7, 8, 9, 7, 8, 9]) == 6

    # def test_exchange_sort_1(self):
    #     print("\n=== Testing Problem 11: Exchange Sort ===")
    #     if exchange_sort is None:
    #         pytest.skip("solution_11.py not found")
    #     assert exchange_sort([9, 9, 7, 7, 8, 8]) == 4

    # def test_exchange_sort_2(self):
    #     if exchange_sort is None:
    #         pytest.skip("solution_11.py not found")
    #     assert exchange_sort([8, 8, 7, 8]) == 1

    # def test_exchange_sort_3(self):
    #     if exchange_sort is None:
    #         pytest.skip("solution_11.py not found")
    #     assert exchange_sort([9, 7, 9]) == 1


class TestProblem12:
    """
    Problem 12: Minimum Total (Triangle)

    Given a triangle, find the minimum path sum from top to bottom.
    Each step you may move to adjacent numbers on the row below.

    Example:
        Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
        Output: 11 (2 + 3 + 5 + 1 = 11)
    """
    

    def test_minimum_total_1(self):
        print("\n=== Testing Problem 12: Minimum Total ===")
        if Solution12 is None:
            pytest.skip("solution_12.py not found")
        solution = Solution12()
        assert solution.minimumTotal([[-10]]) == -10

    def test_minimum_total_2(self):
        if Solution12 is None:
            pytest.skip("solution_12.py not found")
        solution = Solution12()
        assert solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


class TestProblem13:
    """
    Problem 13: Longest Consecutive Sequence

    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    Your algorithm should run in O(n) complexity.

    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: Longest consecutive sequence is [1, 2, 3, 4], length is 4
    """

    def test_longest_consecutive(self):
        print("\n=== Testing Problem 13: Longest Consecutive ===")
        if Solution13 is None:
            pytest.skip("solution_13.py not found")
        solution = Solution13()
        assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


class TestProblem14:
    """
    Problem 14: Longest Common Subsequence

    Given two strings text1 and text2, return the length of their longest common subsequence.
    A subsequence is generated from the original string with some characters deleted
    without changing the relative order.

    Example:
        Input: text1 = "abcde", text2 = "ace"
        Output: 3 (The LCS is "ace" with length 3)
    """

    def test_longest_common_subsequence(self):
        print("\n=== Testing Problem 14: Longest Common Subsequence ===")
        if Solution14 is None:
            pytest.skip("solution_14.py not found")
        solution = Solution14()
        assert solution.longestCommonSubsequence("abcde", "ace") == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=.", "--cov-report=term-missing", "--cov-branch"])

