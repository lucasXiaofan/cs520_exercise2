import pytest
from solution import Solution as Solution1
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


class TestMaxSizeSlices:
    @pytest.mark.parametrize("slices,expected", [
        ([1, 2, 3, 4, 5, 6], 10),
        ([8, 9, 8, 6, 1, 1], 16),
        ([4, 1, 2, 5, 8, 3, 1, 9, 7], 21),
    ])
    def test_max_size_slices(self, slices, expected):
        assert Solution1().maxSizeSlices(slices) == expected


class TestMinSwaps:
    @pytest.mark.parametrize("grid,expected", [
        ([[0,0,1],[1,1,0],[1,0,0]], 3),
        ([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]], -1),
        ([[1,0,0],[1,1,0],[1,1,1]], 0),
    ])
    def test_min_swaps(self, grid, expected):
        assert Solution2().minSwaps(grid) == expected


class TestUnhappyFriends:
    @pytest.mark.parametrize("n,preferences,pairs,expected", [
        (4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]], 2),
        (2, [[1],[0]], [[1,0]], 0),
        (4, [[1,3,2],[2,3,0],[1,3,0],[0,2,1]], [[1,3],[0,2]], 4),
    ])
    def test_unhappy_friends(self, n, preferences, pairs, expected):
        assert Solution3().unhappyFriends(n, preferences, pairs) == expected

