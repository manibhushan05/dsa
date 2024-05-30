def reverse_array(nums, i, j):
    if i > j:
        return
    nums[i], nums[j] = nums[j], nums[i]
    return reverse_array(nums, i + 1, j - 1)


if __name__ == '__main__':
    nums = [1, 2]
    reverse_array(nums, 0, len(nums) - 1)
    print(nums)
