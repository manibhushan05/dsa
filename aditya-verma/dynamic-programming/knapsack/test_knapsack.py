import unittest

from knapsack import knapsack_brute_force, knapsack_memoization


class KnapsackBruteForceTestCase(unittest.TestCase):
    def test_knapsack_zero_capacity(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 0
        assert knapsack_brute_force(len(weights) - 1, weights, values, capacity) == 0

    def test_knapsack_single_item_fit(self):
        weights = [10]
        values = [60]
        capacity = 10
        assert knapsack_brute_force(len(weights) - 1, weights, values, capacity) == 60

    def test_knapsack_single_item_no_fit(self):
        weights = [15]
        values = [60]
        capacity = 10
        assert knapsack_brute_force(len(weights) - 1, weights, values, capacity) == 0

    def test_knapsack_general_case(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        assert knapsack_brute_force(len(weights) - 1, weights, values, capacity) == 220

    def test_knapsack_full_capacity_used(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 60
        assert knapsack_brute_force(len(weights) - 1, weights, values, capacity) == 280


class KnapsackMemoizationTestCase(unittest.TestCase):
    def test_knapsack_zero_capacity(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 0
        assert knapsack_memoization(weights, values, capacity) == 0

    def test_knapsack_single_item_fit(self):
        weights = [10]
        values = [60]
        capacity = 10
        assert knapsack_memoization(weights, values, capacity) == 60

    def test_knapsack_single_item_no_fit(self):
        weights = [15]
        values = [60]
        capacity = 10
        assert knapsack_memoization(weights, values, capacity) == 0

    def test_knapsack_general_case(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        assert knapsack_memoization(weights, values, capacity) == 220

    def test_knapsack_full_capacity_used(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 60
        assert knapsack_memoization(weights, values, capacity) == 280


if __name__ == '__main__':
    unittest.main()
