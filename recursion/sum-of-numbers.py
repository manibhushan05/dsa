def sum_of_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_numbers(n - 1)


if __name__ == '__main__':
    print(sum_of_numbers(10))
