from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxD = 0

        def dfs(elem):
            if not elem:
                return 0

            nonlocal maxD

            maxL = 0
            maxR = 0

            if elem.left:
                maxL = dfs(elem.left)

            if elem.right:
                maxR = dfs(elem.right)

            res = maxR + maxL

            maxD = max(maxD, res)

            return 1 + max(maxR, maxL)

        left = dfs(root)
        right = dfs(root)

        maxD = max(maxD, right + left)

        return maxD
