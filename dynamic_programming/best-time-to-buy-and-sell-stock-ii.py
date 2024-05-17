# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


def brute_force_approach(prices: List[int]) -> int:
    def helper(index, buy):
        if len(prices) == index:
            return 0
        if buy:
            profit = max(-prices[index] + helper(index + 1, False), 0 + helper(index + 1, True))
        else:
            profit = max(prices[index] + helper(index + 1, True), 0 + helper(index + 1, False))
        return profit

    return helper(0, True)


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(brute_force_approach(prices))
