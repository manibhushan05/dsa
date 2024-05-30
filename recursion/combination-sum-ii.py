# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, target):
            if index == len(candidates):
                if target == 0:
                    result.add(tuple(sorted(combination[:])))
                return
            if candidates[index] <= target:
                combination.append(candidates[index])
                helper(index + 1, target - candidates[index])
                combination.pop()
            helper(index + 1, target)

        combination = []
        result = set()
        helper(0, target)
        return [list(row) for row in result]
