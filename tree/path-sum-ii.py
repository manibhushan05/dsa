# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, targetSum, path):
            if node is None:
                return
            path.append(node.val)
            targetSum -= node.val
            if node.left is None and node.right is None:
                if targetSum == 0:
                    result.append(path[:])
            else:
                dfs(node.left, targetSum, path)
                dfs(node.right, targetSum, path)
            path.pop()

        result = []
        dfs(root, targetSum, [])
        return result
