def knapsack_brute_force(index, weights, values, capacity):
    if index == 0:
        if weights[0] <= capacity:
            return values[0]
        else:
            return 0
    not_taken = knapsack_brute_force(index - 1, weights, values, capacity)
    taken = float('-inf')
    if weights[index] <= capacity:
        taken = values[index] + knapsack_brute_force(index - 1, weights, values, capacity - weights[index])
    return max(taken, not_taken)


def knapsack_memoization_util(index, weights, values, capacity, dp):
    if index == 0:
        if weights[0] <= capacity:
            return values[0]
        else:
            return 0
    if dp[index][capacity] != -1:
        return dp[index][capacity]
    not_taken = knapsack_brute_force(index - 1, weights, values, capacity)
    taken = float('-inf')
    if weights[index] <= capacity:
        taken = values[index] + knapsack_brute_force(index - 1, weights, values, capacity - weights[index])
    dp[index][capacity] = max(taken, not_taken)
    return dp[index][capacity]


def knapsack_memoization(weights, values, capacity):
    n = len(weights)
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
    return knapsack_memoization_util(n - 1, weights, values, capacity, dp)


def knapsack_bottom_up(weights, values, capacity):
    pass
