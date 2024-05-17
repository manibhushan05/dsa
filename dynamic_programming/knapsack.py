def knapsack_brute_force_util(index, weights, values, capacity):
    if index == 0:
        if weights[0] <= capacity:
            return values[0]
        else:
            return 0
    not_take = knapsack_brute_force_util(index - 1, weights, values, capacity)
    take = float('-inf')
    if weights[index] <= capacity:
        take = values[index] + knapsack_brute_force_util(index - 1, weights, values, capacity - weights[index])
    return max(take, not_take)


def knapsack_brute_force(weights, values, capacity):
    return knapsack_brute_force_util(len(weights) - 1, weights, values, capacity)


def knapsack_memoization_util(index, weights, values, capacity, dp):
    if index == 0:
        if weights[0] <= capacity:
            return values[0]
        else:
            return 0
    if dp[index][capacity] != -1:
        return dp[index][capacity]
    not_taken = knapsack_memoization_util(index - 1, weights, values, capacity, dp)
    taken = float('-inf')
    if weights[index] <= capacity:
        taken = values[index] + knapsack_memoization_util(index - 1, weights, values, capacity - weights[index], dp)
    dp[index][capacity] = max(taken, not_taken)
    return dp[index][capacity]


def knapsack_memoization(weights, values, capacity):
    n = len(weights)
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
    return knapsack_memoization_util(n - 1, weights, values, capacity, dp)


def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table with dimensions n x W+1 and initialize it with zeros
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Base condition: Fill in the first row for the weight of the first item
    for i in range(weights[0], capacity + 1):
        dp[0][i] = values[0]

    # Fill in the DP table using a bottom-up approach
    for ind in range(1, n):
        for cap in range(capacity + 1):
            # Calculate the maximum value by either excluding the current item or including it
            not_taken = dp[ind - 1][cap]
            taken = float('-inf')

            # Check if the current item can be included without exceeding the knapsack's capacity
            if weights[ind] <= cap:
                taken = values[ind] + dp[ind - 1][cap - weights[ind]]

            # Update the DP table
            dp[ind][cap] = max(not_taken, taken)

    # The final result is in the last cell of the DP table
    return dp[n - 1][capacity]


if __name__ == '__main__':
    weights = [3, 2, 5]
    values = [30, 40, 60]
    capacity = 6
    print(knapsack(weights, values, capacity))
