from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float('-INF')

        def dfs(elem):
            nonlocal res

            if not elem.left and not elem.right:
                res = max(res, elem.val)
                return elem.val

            toReturn = elem.val

            if elem.left:
                l = dfs(elem.left)
                toReturn = max(toReturn, elem.val + l)

            if elem.right:
                r = dfs(elem.right)
                toReturn = max(toReturn, elem.val + r)

            res = max(res, toReturn)

            if elem.left and elem.right:
                res = max(res, elem.val + l + r)

            return toReturn

        x = dfs(root)
        return res


