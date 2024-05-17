def coin_change_recursive_util(index, coins, target):
    if index == 0:
        if target % coins[0] == 0:
            return target // coins[0]
        else:
            return float('inf')
    not_taken = coin_change_recursive_util(index - 1, coins, target)
    taken = float('inf')
    if coins[index] <= target:
        taken = 1 + coin_change_recursive_util(index, coins, target - coins[index])
    return min(taken, not_taken)


def coin_change_recursive(coins, target):
    return coin_change_recursive_util(len(coins) - 1, coins, target)


if __name__ == '__main__':
    coins = [1, 2, 3]
    target = 8
    print(coin_change_recursive(coins, target))
