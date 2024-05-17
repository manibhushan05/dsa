def bs_iterative(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def lower_bound(arr, key):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            result = mid
            end = mid - 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return result


def upper_bound(arr, key):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            result = mid
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return result


def counter(nums):
    res = {}
    for num in nums:
        res[num] = res.get(num, 0) + 1
    max_count = max(res.values())
    for key, val in res.items():
        if val == max_count:
            return key
    return None


print(counter([2, 3, 3, 3, 3, 35]))
