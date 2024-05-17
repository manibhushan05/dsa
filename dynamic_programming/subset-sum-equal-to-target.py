def subset_sum_recursive(arr, index, target):
    if target == 0:
        return True
    if index == 0:
        return arr[0] == target
    not_taken = subset_sum_recursive(arr, index - 1, target)
    taken = False
    if arr[index] <= target:
        taken = subset_sum_recursive(arr, index - 1, target - arr[index])
    return taken or not_taken


print(subset_sum_recursive([1, 2, 3, 4], 3, 4))
