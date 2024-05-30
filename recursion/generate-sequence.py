def generate_sequence(nums, index, res):
    if index == len(nums):
        print(res)
        return
    res.append(nums[index])
    generate_sequence(nums, index + 1, res)
    res.pop()
    generate_sequence(nums, index + 1, res)


if __name__ == '__main__':
    nums = [3, 2, 1]
    generate_sequence(nums, 0, [])
