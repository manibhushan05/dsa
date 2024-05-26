def flatten(nums):
    for num in nums:
        if isinstance(num, list):
            flatten(num)
        else:
            res.append(num)


res = []
flatten([[1, 2, [4, 5]], 3])
print(res)
