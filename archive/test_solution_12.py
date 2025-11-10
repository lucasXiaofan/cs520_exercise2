import pytest
from deepseek_cot_solutions.solution_12 import exchange_sort

def test_exchange_sort():
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

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=.", "--cov-report=term-missing", "--cov-branch"])
