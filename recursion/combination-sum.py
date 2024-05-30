from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, target):
            if index == len(candidates):
                if target == 0:
                    result.append(combination[:])
                return
            if candidates[index] <= target:
                combination.append(candidates[index])
                helper(index, target - candidates[index])
                combination.pop()
            helper(index + 1, target)

        combination = []
        result = []
        helper(0, target)
        return result
