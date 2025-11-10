"""
Comprehensive test suite for solution_12.py (Exchange Sort)
Uses pytest for complete line and branch coverage

Run tests with:
    pytest test_solution_12_comprehensive.py -v

Run with coverage:
    pytest test_solution_12_comprehensive.py -v --cov=deepseek_cot_solutions/solution_12 --cov-report=term-missing --cov-branch
"""

import pytest
from deepseek_cot_solutions.solution_12 import exchange_sort


class TestExchangeSort:
    """
    Test suite for the exchange_sort function.
    
    Problem: Given a sequence (length <= 1000) of 3 different key values (7, 8, 9),
    find the minimum number of exchange operations to make the sequence sorted.
    One operation is switching 2 key values.
    """

    def test_empty_sequence(self):
        """Test empty sequence - covers for loop with range(0)"""
        assert exchange_sort([]) == 0

    def test_single_element(self):
        """Test single element - covers range(1) and if condition being false"""
        assert exchange_sort([7]) == 0
        assert exchange_sort([8]) == 0
        assert exchange_sort([9]) == 0

    def test_already_sorted(self):
        """Test already sorted sequences - all if conditions at line 7 are false"""
        assert exchange_sort([7, 7, 8, 8, 9, 9]) == 0
        assert exchange_sort([7, 8, 9]) == 0
        assert exchange_sort([7, 8, 8, 8, 9, 9, 9]) == 0
        assert exchange_sort([7, 7, 7, 8, 8, 9, 9, 9]) == 0

    def test_single_swap_needed(self):
        """Test cases where a single swap is needed"""
        # Swap adjacent elements
        assert exchange_sort([7, 8, 7, 8, 9, 9]) == 1
        # Swap first two elements
        assert exchange_sort([8, 7, 8, 8, 9, 9]) == 1
        # Swap last two elements
        assert exchange_sort([7, 7, 8, 9, 8, 9]) == 1
        # Swap non-adjacent elements
        assert exchange_sort([7, 9, 8]) == 1
        assert exchange_sort([9, 7, 8]) == 1
        assert exchange_sort([8, 7, 9]) == 1

    def test_two_swaps_needed(self):
        """Test cases where two swaps are needed"""
        assert exchange_sort([7, 9, 8, 7, 8, 9]) == 2
        assert exchange_sort([8, 7, 9, 8, 7, 9]) == 2
        assert exchange_sort([9, 8, 7, 9, 8, 7]) == 2

    def test_three_swaps_needed(self):
        """Test cases where three swaps are needed"""
        assert exchange_sort([8, 9, 7, 8, 9, 7]) == 3
        assert exchange_sort([9, 7, 9, 8, 7, 8]) == 3

    def test_four_swaps_needed(self):
        """Test the example from problem description"""
        assert exchange_sort([9, 9, 7, 7, 8, 8]) == 4

    def test_six_swaps_needed(self):
        """Test a more complex case"""
        assert exchange_sort([7, 8, 9, 7, 8, 9, 7, 8, 9]) == 6

    def test_all_same_value(self):
        """Test sequences with only one value type - all if conditions false"""
        assert exchange_sort([7, 7, 7, 7]) == 0
        assert exchange_sort([8, 8, 8, 8, 8]) == 0
        assert exchange_sort([9, 9, 9]) == 0
        assert exchange_sort([7]) == 0

    def test_alternating_pattern(self):
        """Test alternating patterns"""
        assert exchange_sort([7, 8, 7, 8, 7, 8]) == 3
        assert exchange_sort([8, 9, 8, 9, 8, 9]) == 3
        assert exchange_sort([7, 9, 7, 9, 7, 9]) == 3
        assert exchange_sort([9, 7, 9, 7, 9, 7]) == 3

    def test_reverse_sorted(self):
        """Test reverse sorted sequences"""
        assert exchange_sort([9, 9, 8, 8, 7, 7]) == 3
        assert exchange_sort([9, 8, 7]) == 2

    def test_longer_sequences(self):
        """Test with longer sequences to ensure loop works correctly"""
        # Length 10
        assert exchange_sort([9, 7, 8, 9, 7, 8, 9, 7, 8, 7]) == 5
        # Length 15
        assert exchange_sort([7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8]) == 10

    def test_edge_case_beginning_misplaced(self):
        """Test when first element is misplaced"""
        assert exchange_sort([9, 7, 7, 8, 8, 9]) == 3
        assert exchange_sort([8, 7, 7, 8, 9, 9]) == 1

    def test_edge_case_end_misplaced(self):
        """Test when last element is misplaced"""
        assert exchange_sort([7, 7, 8, 8, 9, 9]) == 0
        assert exchange_sort([7, 7, 8, 9, 8, 9]) == 1
        assert exchange_sort([7, 8, 8, 8, 9, 7]) == 1

    def test_middle_elements_misplaced(self):
        """Test when middle elements are misplaced"""
        assert exchange_sort([7, 9, 7, 8, 8, 9]) == 2
        assert exchange_sort([7, 7, 9, 8, 8, 9]) == 1

    def test_multiple_swaps_same_position(self):
        """Test cases where multiple swaps happen at different positions"""
        # This tests that the loop continues after swaps
        result = exchange_sort([9, 8, 7, 9, 8, 7, 9, 8, 7])
        assert result == 9  # 3 groups of 3 elements each need 3 swaps

    @pytest.mark.parametrize("sequence,expected", [
        # Edge cases
        ([], 0),
        ([7], 0),
        ([8], 0),
        ([9], 0),
        
        # Already sorted
        ([7, 8, 9], 0),
        ([7, 7, 8, 8, 9, 9], 0),
        ([7, 7, 7, 8, 8, 9, 9, 9], 0),
        
        # Single swap
        ([8, 7, 8, 8, 9, 9], 1),
        ([7, 7, 8, 9, 8, 9], 1),
        ([9, 7, 8], 1),
        ([7, 9, 8], 1),
        
        # Two swaps
        ([7, 9, 8, 7, 8, 9], 2),
        ([8, 7, 9, 8, 7, 9], 2),
        
        # Example from problem
        ([9, 9, 7, 7, 8, 8], 4),
        
        # All same value
        ([7, 7, 7, 7], 0),
        ([8, 8, 8, 8], 0),
        ([9, 9, 9, 9], 0),
    ])
    def test_parametrized_cases(self, sequence, expected):
        """Parametrized test for common cases"""
        assert exchange_sort(sequence) == expected

    def test_branch_coverage_inner_while_loop(self):
        """
        Test to ensure the inner while loop condition is fully covered.
        This tests both the continuation condition and exit condition.
        """
        # Case where j needs to search and finds the element
        # [7, 8, 9, 7] -> needs 2 swaps
        # At i=0: seq[0]=7, sorted[0]=7, so no swap
        # At i=1: seq[1]=8, sorted[1]=7, need to find 7
        # j starts at 2, seq[2]=9 != 7, j=3, seq[3]=7 == 7, found!
        assert exchange_sort([7, 8, 9, 7]) == 2

        # Another case to test the while loop logic
        # [9, 7, 8, 7] -> needs 2 swaps
        # At i=0: seq[0]=9, sorted[0]=7, need to find 7
        # j starts at 1, seq[1]=7 == 7, found immediately
        assert exchange_sort([9, 7, 8, 7]) == 2

    def test_preserves_input(self):
        """Test that the function doesn't modify the original sequence"""
        original = [9, 9, 7, 7, 8, 8]
        exchange_sort(original)
        assert original == [9, 9, 7, 7, 8, 8]

    def test_return_type(self):
        """Test that the function returns an integer"""
        result = exchange_sort([9, 9, 7, 7, 8, 8])
        assert isinstance(result, int)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=deepseek_cot_solutions/solution_12", 
                 "--cov-report=term-missing", "--cov-branch"])
