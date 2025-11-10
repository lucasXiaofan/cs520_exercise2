"""
Test file for individual solution coverage testing

This file tests each of the 40 solution files individually to measure
coverage for each LLM+prompt combination separately.
"""

import pytest
import sys
from pathlib import Path

# Add individual_solutions to path
sys.path.insert(0, str(Path(__file__).parent / "individual_solutions"))


# ========== Problem 2: Maximum Pizza Slices ==========
class TestSolution02:
    """Maximum Pizza Slices"""

    def test_02_deepseek_cot(self):
        """Test solution_02_deepseek_cot"""
        from solution_02_deepseek_cot import maxSizeSlices
        assert maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10

    def test_02_deepseek_self_planning(self):
        """Test solution_02_deepseek_self_planning"""
        from solution_02_deepseek_self_planning import maxSizeSlices
        assert maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10

    def test_02_gemini_cot(self):
        """Test solution_02_gemini_cot"""
        from solution_02_gemini_cot import maxSizeSlices
        assert maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10

    def test_02_gemini_self_planning(self):
        """Test solution_02_gemini_self_planning"""
        from solution_02_gemini_self_planning import maxSizeSlices
        assert maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10


# ========== Problem 3: Number of Times All Blue ==========
class TestSolution03:
    """Number of Times All Blue"""

    def test_03_deepseek_cot(self):
        """Test solution_03_deepseek_cot"""
        from solution_03_deepseek_cot import numTimesAllBlue
        assert numTimesAllBlue([2, 1, 3, 5, 4]) == 3

    def test_03_deepseek_self_planning(self):
        """Test solution_03_deepseek_self_planning"""
        from solution_03_deepseek_self_planning import numTimesAllBlue
        assert numTimesAllBlue([2, 1, 3, 5, 4]) == 3

    def test_03_gemini_cot(self):
        """Test solution_03_gemini_cot"""
        from solution_03_gemini_cot import numTimesAllBlue
        result = numTimesAllBlue([2, 1, 3, 5, 4])
        assert result == 3

    def test_03_gemini_self_planning(self):
        """Test solution_03_gemini_self_planning"""
        from solution_03_gemini_self_planning import numTimesAllBlue
        assert numTimesAllBlue([2, 1, 3, 5, 4]) == 3


# ========== Problem 4: Unhappy Friends ==========
class TestSolution04:
    """Unhappy Friends"""

    def test_04_deepseek_cot(self):
        """Test solution_04_deepseek_cot"""
        from solution_04_deepseek_cot import unhappyFriends
        assert unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]) == 2

    def test_04_deepseek_self_planning(self):
        """Test solution_04_deepseek_self_planning"""
        from solution_04_deepseek_self_planning import unhappyFriends
        assert unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]) == 2

    def test_04_gemini_cot(self):
        """Test solution_04_gemini_cot"""
        from solution_04_gemini_cot import unhappyFriends
        assert unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]) == 2

    def test_04_gemini_self_planning(self):
        """Test solution_04_gemini_self_planning"""
        from solution_04_gemini_self_planning import unhappyFriends
        assert unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]) == 2


# ========== Problem 5: Minimum Swaps to Make Grid Valid ==========
class TestSolution05:
    """Minimum Swaps to Make Grid Valid"""

    def test_05_deepseek_cot(self):
        """Test solution_05_deepseek_cot"""
        from solution_05_deepseek_cot import minSwaps
        assert minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3

    def test_05_deepseek_self_planning(self):
        """Test solution_05_deepseek_self_planning"""
        from solution_05_deepseek_self_planning import minSwaps
        assert minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3

    def test_05_gemini_cot(self):
        """Test solution_05_gemini_cot"""
        from solution_05_gemini_cot import minSwaps
        result = minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]])
        assert result == 3

    def test_05_gemini_self_planning(self):
        """Test solution_05_gemini_self_planning"""
        from solution_05_gemini_self_planning import minSwaps
        assert minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3


# ========== Problem 6: Mix Strings ==========
class TestSolution06:
    """Mix Strings"""

    def test_06_deepseek_cot_case1(self):
        """Test solution_06_deepseek_cot case 1"""
        from solution_06_deepseek_cot import mix
        assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    def test_06_deepseek_cot_case2(self):
        """Test solution_06_deepseek_cot case 2"""
        from solution_06_deepseek_cot import mix
        assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"

    def test_06_deepseek_cot_case3(self):
        """Test solution_06_deepseek_cot case 3"""
        from solution_06_deepseek_cot import mix
        assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"

    def test_06_deepseek_self_planning_case1(self):
        """Test solution_06_deepseek_self_planning case 1"""
        from solution_06_deepseek_self_planning import mix
        assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    def test_06_deepseek_self_planning_case2(self):
        """Test solution_06_deepseek_self_planning case 2"""
        from solution_06_deepseek_self_planning import mix
        assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"

    def test_06_deepseek_self_planning_case3(self):
        """Test solution_06_deepseek_self_planning case 3"""
        from solution_06_deepseek_self_planning import mix
        assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"

    def test_06_gemini_cot_case1(self):
        """Test solution_06_gemini_cot case 1"""
        from solution_06_gemini_cot import mix
        result = mix("looping is fun but dangerous", "less dangerous than coding")
        assert result == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    def test_06_gemini_cot_case2(self):
        """Test solution_06_gemini_cot case 2"""
        from solution_06_gemini_cot import mix
        result = mix("Are they here", "yes, they are here")
        assert result == "2:eeeee/2:yy/=:hh/=:rr"

    def test_06_gemini_cot_case3(self):
        """Test solution_06_gemini_cot case 3"""
        from solution_06_gemini_cot import mix
        result = mix("Lords of the Fallen", "gamekult")
        assert result == "1:ee/1:ll/1:oo"

    def test_06_gemini_self_planning_case1(self):
        """Test solution_06_gemini_self_planning case 1"""
        from solution_06_gemini_self_planning import mix
        result = mix("looping is fun but dangerous", "less dangerous than coding")
        assert result == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    def test_06_gemini_self_planning_case2(self):
        """Test solution_06_gemini_self_planning case 2"""
        from solution_06_gemini_self_planning import mix
        result = mix("Are they here", "yes, they are here")
        assert result == "2:eeeee/2:yy/=:hh/=:rr"

    def test_06_gemini_self_planning_case3(self):
        """Test solution_06_gemini_self_planning case 3"""
        from solution_06_gemini_self_planning import mix
        result = mix("Lords of the Fallen", "gamekult")
        assert result == "1:ee/1:ll/1:oo"


# ========== Problem 7: Contains Cycle in Grid ==========
class TestSolution07:
    """Contains Cycle in Grid"""

    def test_07_deepseek_cot(self):
        """Test solution_07_deepseek_cot"""
        from solution_07_deepseek_cot import containsCycle
        assert containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True

    def test_07_deepseek_self_planning(self):
        """Test solution_07_deepseek_self_planning"""
        from solution_07_deepseek_self_planning import containsCycle
        assert containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True

    def test_07_gemini_cot(self):
        """Test solution_07_gemini_cot"""
        from solution_07_gemini_cot import containsCycle
        assert containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True

    def test_07_gemini_self_planning(self):
        """Test solution_07_gemini_self_planning"""
        from solution_07_gemini_self_planning import containsCycle
        assert containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True


# ========== Problem 8: Number of Permutations with DI Sequence ==========
class TestSolution08:
    """Number of Permutations with DI Sequence"""

    def test_08_deepseek_cot(self):
        """Test solution_08_deepseek_cot"""
        from solution_08_deepseek_cot import numPermsDISequence
        assert numPermsDISequence("DID") == 5

    def test_08_deepseek_self_planning(self):
        """Test solution_08_deepseek_self_planning"""
        from solution_08_deepseek_self_planning import numPermsDISequence
        assert numPermsDISequence("DID") == 5

    def test_08_gemini_cot(self):
        """Test solution_08_gemini_cot"""
        from solution_08_gemini_cot import numPermsDISequence
        result = numPermsDISequence("DID")
        assert result == 5

    def test_08_gemini_self_planning(self):
        """Test solution_08_gemini_self_planning"""
        from solution_08_gemini_self_planning import numPermsDISequence
        assert numPermsDISequence("DID") == 5


# ========== Problem 10: Least Operators to Express Target ==========
class TestSolution10:
    """Least Operators to Express Target"""

    def test_10_deepseek_cot(self):
        """Test solution_10_deepseek_cot"""
        from solution_10_deepseek_cot import leastOpsExpressTarget
        assert leastOpsExpressTarget(3, 19) == 5

    def test_10_deepseek_self_planning(self):
        """Test solution_10_deepseek_self_planning"""
        from solution_10_deepseek_self_planning import leastOpsExpressTarget
        assert leastOpsExpressTarget(3, 19) == 5

    def test_10_gemini_cot(self):
        """Test solution_10_gemini_cot"""
        from solution_10_gemini_cot import leastOpsExpressTarget
        result = leastOpsExpressTarget(3, 19)
        assert result == 5

    def test_10_gemini_self_planning(self):
        """Test solution_10_gemini_self_planning"""
        from solution_10_gemini_self_planning import leastOpsExpressTarget
        result = leastOpsExpressTarget(3, 19)
        assert result == 5


# ========== Problem 11: Longest Common Subsequence ==========
class TestSolution11:
    """Longest Common Subsequence"""

    def test_11_deepseek_cot(self):
        """Test solution_11_deepseek_cot"""
        from solution_11_deepseek_cot import longestCommonSubsequence
        assert longestCommonSubsequence("abcde", "ace") == 3

    def test_11_deepseek_self_planning(self):
        """Test solution_11_deepseek_self_planning"""
        from solution_11_deepseek_self_planning import longestCommonSubsequence
        assert longestCommonSubsequence("abcde", "ace") == 3

    def test_11_gemini_cot(self):
        """Test solution_11_gemini_cot"""
        from solution_11_gemini_cot import longestCommonSubsequence
        result = longestCommonSubsequence("abcde", "ace")
        assert result == 3

    def test_11_gemini_self_planning(self):
        """Test solution_11_gemini_self_planning"""
        from solution_11_gemini_self_planning import longestCommonSubsequence
        assert longestCommonSubsequence("abcde", "ace") == 3


# ========== Problem 12: Exchange Sort ==========
class TestSolution12:
    """Exchange Sort"""

    def test_12_deepseek_cot_case1(self):
        """Test solution_12_deepseek_cot case 1"""
        from solution_12_deepseek_cot import exchangeSort
        assert exchangeSort([9, 9, 7, 7, 8, 8]) == 4

    def test_12_deepseek_cot_case2(self):
        """Test solution_12_deepseek_cot case 2"""
        from solution_12_deepseek_cot import exchangeSort
        assert exchangeSort([8, 8, 7, 8]) == 1

    def test_12_deepseek_cot_case3(self):
        """Test solution_12_deepseek_cot case 3"""
        from solution_12_deepseek_cot import exchangeSort
        assert exchangeSort([9, 7, 9]) == 1

    def test_12_deepseek_self_planning_case1(self):
        """Test solution_12_deepseek_self_planning case 1"""
        from solution_12_deepseek_self_planning import exchangeSort
        assert exchangeSort([9, 9, 7, 7, 8, 8]) == 4

    def test_12_deepseek_self_planning_case2(self):
        """Test solution_12_deepseek_self_planning case 2"""
        from solution_12_deepseek_self_planning import exchangeSort
        assert exchangeSort([8, 8, 7, 8]) == 1

    def test_12_deepseek_self_planning_case3(self):
        """Test solution_12_deepseek_self_planning case 3"""
        from solution_12_deepseek_self_planning import exchangeSort
        assert exchangeSort([9, 7, 9]) == 1

    def test_12_gemini_cot_case1(self):
        """Test solution_12_gemini_cot case 1"""
        from solution_12_gemini_cot import exchangeSort
        assert exchangeSort([9, 9, 7, 7, 8, 8]) == 4

    def test_12_gemini_cot_case2(self):
        """Test solution_12_gemini_cot case 2"""
        from solution_12_gemini_cot import exchangeSort
        assert exchangeSort([8, 8, 7, 8]) == 1

    def test_12_gemini_cot_case3(self):
        """Test solution_12_gemini_cot case 3"""
        from solution_12_gemini_cot import exchangeSort
        assert exchangeSort([9, 7, 9]) == 1

    def test_12_gemini_self_planning_case1(self):
        """Test solution_12_gemini_self_planning case 1"""
        from solution_12_gemini_self_planning import exchangeSort
        assert exchangeSort([9, 9, 7, 7, 8, 8]) == 4

    def test_12_gemini_self_planning_case2(self):
        """Test solution_12_gemini_self_planning case 2"""
        from solution_12_gemini_self_planning import exchangeSort
        assert exchangeSort([8, 8, 7, 8]) == 1

    def test_12_gemini_self_planning_case3(self):
        """Test solution_12_gemini_self_planning case 3"""
        from solution_12_gemini_self_planning import exchangeSort
        assert exchangeSort([9, 7, 9]) == 1
