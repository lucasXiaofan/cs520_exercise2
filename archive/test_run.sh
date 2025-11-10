#!/bin/bash

echo "=========================================="
echo "Problem 1: Max Size Slices"
echo "=========================================="
uv run pytest test_solution.py --cov=solution --cov-branch --cov-report=term-missing
echo -e "\n=========================================="
echo "Problem 2: Min Swaps"
echo "=========================================="
uv run pytest test_solution.py --cov=solution2 --cov-branch --cov-report=term-missing

echo -e "\n=========================================="
echo "Problem 3: Unhappy Friends"
echo "=========================================="
uv run pytest test_solution.py --cov=solution3 --cov-branch --cov-report=term-missing