'''

Given an unsorted integer array, print all greater elements than all elements present to their right.

Input : [10, 4, 6, 3, 5]
Output: [10, 6, 5]
Explanation: The elements that are greater than all elements to their right are 10, 6, and 5.

Note: The solution should return the elements in the same order as they appear in the input array.

'''
from collections import deque
from typing import List

import pytest


class Solution:
    def findGreaterElements(self, nums: List[int]) -> List[int]:
        # base case
        if not nums:
            return []
        # create an empty stack
        stack = deque()
        for i in range(len(nums)):
            # pop all elements that are less than current elements
            while stack and nums[i] > stack[-1]:
                stack.pop()
            # push current element to stack
            stack.append(nums[i])
        return list(stack)


def test_greater_number():
    assert Solution().findGreaterElements(nums=[10, 4, 6, 3, 5]) == [10, 6, 5]


if __name__ == '__main__':
    pytest.main()
