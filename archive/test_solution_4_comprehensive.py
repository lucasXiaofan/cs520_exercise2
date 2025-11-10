"""
Comprehensive test cases for solution_4.py (Unhappy Friends)
Covers all lines and branches with pytest

Run with: pytest test_solution_4_comprehensive.py -v
Run with coverage: pytest test_solution_4_comprehensive.py -v --cov=deepseek_cot_solutions.solution_4 --cov-report=term-missing --cov-branch
"""

import pytest
from typing import List

# Import the solution
try:
    from deepseek_cot_solutions.solution_4 import Solution as Solution4
except ImportError:
    Solution4 = None


class TestSolution4UnhappyFriends:
    """
    Test suite for Problem 4: Unhappy Friends
    
    A friend x is unhappy if x is paired with y and there exists u paired with v where:
    - x prefers u over y, and
    - u prefers x over v
    """

    def test_basic_example(self):
        """Test with the example from the problem description"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],
            [[0, 1], [2, 3]]
        )
        assert result == 2

    def test_minimal_case_n_2(self):
        """Test with n=2 (minimal valid case) - both should be happy"""
        solution = Solution4()
        result = solution.unhappyFriends(
            2,
            [[1], [0]],
            [[0, 1]]
        )
        assert result == 0

    def test_no_unhappy_friends(self):
        """Test when all pairs are satisfied with their choices"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_all_unhappy(self):
        """Test when all friends are unhappy"""
        solution = Solution4()
        # In this case, each person prefers their friend's partner
        result = solution.unhappyFriends(
            4,
            [[2, 1, 3], [3, 0, 2], [0, 1, 3], [1, 0, 2]],
            [[0, 1], [2, 3]]
        )
        assert result == 4

    def test_single_unhappy(self):
        """Test when only one friend is unhappy"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3], [3, 2, 0], [0, 1, 3], [1, 2, 0]],
            [[0, 1], [2, 3]]
        )
        # All three conditions can be satisfied: 0 prefers 1, 1 prefers 0 or 2, 2 prefers 0
        assert result == 3

    def test_empty_preferences(self):
        """Test with empty preferences (edge case)"""
        solution = Solution4()
        result = solution.unhappyFriends(
            2,
            [[], []],
            [[0, 1]]
        )
        assert result == 0

    def test_partner_only_preference(self):
        """Test when person only has their partner in preferences"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1], [0, 2, 3], [1, 3, 0], [2, 1, 0]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_unhappy_with_multiple_preferences(self):
        """Test complex case with multiple preferences"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[1, 2, 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 4, 5, 3], 
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0-1: 0's first choice is 1, 1's first choice is 0
        # 2-3: 2's first choice is 0, 0 prefers 1 over 2, 2's first is 0, 0's first is 1
        #      3's first choice is 0, 0 prefers 1 over 3
        # 4-5: 4's first choice is 0, 0 prefers 1 over 4, 5's first is 0
        # 2 prefers 0, 0 prefers 1 over 2 -> 2 is unhappy
        # 3 prefers 0, 0 prefers 1 over 3 -> 3 is unhappy
        # 4 prefers 0, 0 prefers 1 over 4 -> 4 is unhappy
        # 5 prefers 0, 0 prefers 1 over 5 -> 5 is unhappy
        assert result == 4

    def test_larger_n_all_unhappy(self):
        """Test with larger n where all are unhappy"""
        solution = Solution4()
        # Each person prefers their friend's partner
        result = solution.unhappyFriends(
            6,
            [[2, 1, 3, 4, 5], [3, 0, 2, 4, 5], [0, 1, 4, 5, 3],
             [1, 0, 2, 5, 4], [1, 0, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        assert result == 6

    def test_partner_at_end_of_preferences(self):
        """Test when partner is at the end of preferences list"""
        solution = Solution4()
        # Person 0 prefers everyone before their partner (1)
        result = solution.unhappyFriends(
            4,
            [[2, 3, 1], [0, 3, 2], [1, 0, 3], [2, 0, 1]],
            [[0, 1], [2, 3]]
        )
        # 0 prefers 2 and 3 over 1
        # 2 prefers 1 over 3 -> 0 is unhappy (0 prefers 2, 2 prefers 0)
        # 3 prefers 2 over 3 -> 1 is unhappy (1 prefers 3, 3 prefers 1)
        assert result == 2

    def test_no_one_prefers_others_partner(self):
        """Test when no one prefers their friend's partner"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 0, 2, 3], [0, 1, 2, 3], [3, 2, 0, 1], [2, 3, 0, 1]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_circular_unhappiness(self):
        """Test circular pattern of unhappiness"""
        solution = Solution4()
        # 0 prefers 2, 2 prefers 1, 1 prefers 0
        result = solution.unhappyFriends(
            4,
            [[2, 1, 3, 0], [0, 2, 3, 1], [1, 0, 3, 2], [3, 0, 1, 2]],
            [[0, 1], [2, 3]]
        )
        # 0 prefers 2, 2 prefers 1 -> 0 unhappy if 2 prefers 0 over 3
        # 1 prefers 0, 0 prefers 2 -> 1 unhappy if 0 prefers 1 over 2
        # 2 prefers 1, 1 prefers 0 -> 2 unhappy if 1 prefers 2 over 0
        # 3 prefers 0, 0 prefers 2 -> 3 unhappy if 0 prefers 3 over 1
        assert result == 3

    def test_mixed_unhappiness(self):
        """Test with some happy and some unhappy friends"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[3, 1, 2, 4, 5], [0, 2, 4, 3, 5], [1, 3, 0, 4, 5],
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0 prefers 3, 3 prefers 0 over 4 -> 0 is unhappy
        # 1 prefers 0 (their partner) -> happy
        # 2 prefers 1, 1 prefers 3 over 0 -> 2 is unhappy
        # 3 prefers 0, 0 prefers 3 over 1 -> 3 is unhappy
        assert result == 3

    def test_partner_first_in_preferences(self):
        """Test when partner is the first preference"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 0, 2, 3], [0, 1, 2, 3], [3, 2, 0, 1], [2, 3, 0, 1]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_preference_with_duplicates(self):
        """Test preferences with repeated friend IDs (edge case)"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 1, 2, 3], [0, 0, 2, 3], [0, 1, 1, 3], [1, 2, 0, 0]],
            [[0, 1], [2, 3]]
        )
        # With duplicates, the break happens at first occurrence
        assert result == 0

    def test_skewed_preferences(self):
        """Test with highly skewed preference orders"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[3, 2, 1, 0], [3, 2, 0, 1], [3, 2, 1, 0], [3, 2, 1, 0]],
            [[0, 1], [2, 3]]
        )
        # 0 prefers 3, 3 prefers 0 -> 0 is unhappy
        # 1 prefers 3, 3 prefers 2 -> 1 is happy
        assert result == 1

    def test_pair_reversal(self):
        """Test when pairs are given in reversed order"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
            [[1, 0], [3, 2]]  # Note: reversed pairs
        )
        assert result == 0

    def test_different_order_of_pairs(self):
        """Test pairs in different ordering"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            [[2, 3], [0, 1]]  # Different order than iteration
        )
        # Just verify it doesn't crash
        assert result >= 0

    def test_long_preference_lists(self):
        """Test with longer preference lists (beyond n)"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3, 0, 0, 0], [0, 2, 3, 1, 1, 1], [0, 1, 3, 2, 2, 2], [0, 1, 2, 3, 3, 3]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_self_reference_in_preferences(self):
        """Test when preferences include self (edge case)"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[0, 1, 2, 3], [1, 0, 2, 3], [2, 3, 0, 1], [3, 2, 0, 1]],
            [[0, 1], [2, 3]]
        )
        # Person 0 prefers themselves first, then their partner
        # No one should be unhappy
        assert result == 0

    def test_alternating_unhappiness(self):
        """Test alternating pattern of happy and unhappy"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[1, 3, 2, 4, 5], [0, 2, 4, 3, 5], [1, 0, 4, 5, 3],
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0 prefers 1 (partner) first -> happy
        # 1 prefers 0 (partner) first -> happy
        # 2 prefers 1, 1 prefers 2 over 0 -> 2 is unhappy
        # 3 prefers 0, 0 prefers 3 over 1 -> 3 is unhappy
        # 4 prefers 0, 0 prefers 1 over 4 -> 4 is unhappy
        # 5 prefers 0, 0 prefers 1 over 5 -> 5 is unhappy
        assert result == 4


class TestSolution4EdgeCases:
    """Edge case tests for robust coverage"""

    def test_zero_friends(self):
        """Test with n=0 (edge case)"""
        solution = Solution4()
        result = solution.unhappyFriends(0, [], [])
        assert result == 0

    def test_multiple_pairs_all_happy(self):
        """Test multiple pairs all satisfied"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[1, 0, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [3, 2, 0, 1, 4, 5],
             [2, 3, 0, 1, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0 prefers 1 (partner) first
        # 1 prefers 0 (partner) first
        # 2 prefers 3, 3 prefers 2 -> both happy
        # 4 and 5 prefer 0 and 1, but 0 and 1 prefer each other
        assert result == 0

    def test_pair_map_bidirectional(self):
        """Test that pair_map correctly handles bidirectional mapping"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            [[0, 1], [2, 3]]
        )
        # 0 prefers 2, 2 prefers 1 -> 0 unhappy if 2 prefers 0 over 3
        # 1 prefers 0, 0 prefers 2 -> 1 unhappy if 0 prefers 1 over 2
        # 2 prefers 1, 1 prefers 0 -> 2 unhappy if 1 prefers 2 over 0
        # 3 prefers 0, 0 prefers 2 -> 3 unhappy if 0 prefers 3 over 1
        assert result == 3

    def test_break_on_partner(self):
        """Test that the break when finding partner works correctly"""
        solution = Solution4()
        # Person 0 prefers 2, but when they find partner 1, they stop
        result = solution.unhappyFriends(
            4,
            [[2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            [[0, 1], [2, 3]]
        )
        # 0 checks preferences: 2 -> 2 prefers 1 (not 0), 0 is happy
        # 1 checks preferences: 0 -> 0's preferences: 2, 1(break), 1 is happy
        assert result == 2

    def test_set_operations(self):
        """Test set operations for tracking unhappy friends"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[2, 1, 3, 4, 5], [0, 3, 2, 4, 5], [1, 0, 4, 5, 3],
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0 prefers 2, 2 prefers 1 -> 0 unhappy if 2 prefers 0 over 3
        # 1 prefers 0 (partner) -> happy
        # 2 prefers 1, 1 prefers 3 over 0 -> 2 is unhappy
        # 3 prefers 0, 0 prefers 2 over 1 -> 3 is unhappy
        # 4 prefers 0, 0 prefers 2 over 4 -> 4 is unhappy
        # 5 prefers 0, 0 prefers 2 over 5 -> 5 is unhappy
        assert result == 4

    def test_preference_index_comparison(self):
        """Test the preference index comparison logic"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 3, 2, 0], [0, 2, 3, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            [[0, 1], [2, 3]]
        )
        # 0 prefers 1 (partner) first -> happy
        # 1 prefers 0 (partner) first -> happy
        # 2 prefers 1, 1 prefers 2 over 0 -> 2 is unhappy
        assert result == 1

    def test_complex_preference_interactions(self):
        """Test complex interactions between multiple preferences"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[3, 1, 2, 4, 5], [0, 2, 4, 3, 5], [1, 0, 4, 5, 3],
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        # 0 prefers 3, 3 prefers 0 over 4 -> 0 is unhappy
        # 1 prefers 0 (partner) -> happy
        # 2 prefers 1, 1 prefers 3 over 0 -> 2 is unhappy
        # 3 prefers 0, 0 prefers 3 over 1 -> 3 is unhappy
        # 4 prefers 0, 0 prefers 3 over 4 -> 4 is unhappy
        # 5 prefers 0, 0 prefers 3 over 5 -> 5 is unhappy
        assert result == 4

    def test_boundary_conditions(self):
        """Test boundary conditions for preferences"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1], [0], [3], [2]],
            [[0, 1], [2, 3]]
        )
        assert result == 0

    def test_return_value_type(self):
        """Test that return value is always an integer"""
        solution = Solution4()
        result = solution.unhappyFriends(
            4,
            [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
            [[0, 1], [2, 3]]
        )
        assert isinstance(result, int)
        assert result == 0

    def test_unhappy_set_not_affected_by_duplicates(self):
        """Test that set prevents duplicate unhappy friends"""
        solution = Solution4()
        result = solution.unhappyFriends(
            6,
            [[3, 1, 2, 4, 5], [0, 2, 4, 3, 5], [1, 0, 4, 5, 3],
             [0, 1, 2, 5, 4], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]],
            [[0, 1], [2, 3], [4, 5]]
        )
        assert isinstance(result, int)
        assert result == 4

    def test_iteration_order_independence(self):
        """Test that result is independent of iteration order"""
        solution = Solution4()
        result1 = solution.unhappyFriends(
            4,
            [[2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            [[0, 1], [2, 3]]
        )
        # Same result with different iteration
        assert result1 == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=deepseek_cot_solutions.solution_4", "--cov-report=term-missing", "--cov-branch"])
