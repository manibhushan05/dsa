def binary_search_iterative(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search_recursive(nums, low, mid - 1, target)
    else:
        return binary_search_recursive(nums, mid + 1, high, target)


print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7], 0, 6, 4))
