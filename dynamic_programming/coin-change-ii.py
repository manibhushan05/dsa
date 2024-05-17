def coin_change_recursive_util(index, coins, target):
    if index == 0:
        if target % coins[0] == 0:
            return 1
        else:
            return 0
    not_taken = coin_change_recursive_util(index - 1, coins, target)
    taken = 0
    if coins[index] <= target:
        taken = coin_change_recursive_util(index, coins, target - coins[index])
    return taken + not_taken


def coin_change_recursive(coins, target):
    return coin_change_recursive_util(len(coins) - 1, coins, target)


def outer():
    x = "local"

    def inner(n):
        if n == 0:
            return
        nonlocal x
        inner(n - 1)
        x = "mani"
        print("Inner:", x)


    inner(3)
    print("Outer:", x)


if __name__ == '__main__':
    # print(coin_change_recursive([1, 2, 3], 4))
    outer()
