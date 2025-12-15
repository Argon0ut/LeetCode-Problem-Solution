from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0

        def dfs(elem, counter):
            if not elem:
                return
            counter += 1
            nonlocal res

            if not elem.left and not elem.right:
                res = max(res, counter)
                return

            if elem.left:
                dfs(elem.left, counter)
            if elem.right:
                dfs(elem.right, counter)

        dfs(root, 0)
        return res
