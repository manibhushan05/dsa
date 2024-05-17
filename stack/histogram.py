from typing import List


def histogram_brute(heights: List) -> int:
    start, end = 0, len(heights) - 1
    res = 0
    for i in range(len(heights)):
        left = i
        right = i
        while left >= start and heights[i] <= heights[left]:
            left -= 1
        while right <= end and heights[i] <= heights[right]:
            right += 1
        temp = (right - left - 1) * heights[i]
        if temp > res:
            res = temp
    return res


print(histogram_brute([2, 1, 5, 6, 2, 3]))
