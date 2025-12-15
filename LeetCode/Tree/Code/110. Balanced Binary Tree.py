from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        res = True

        def dfs(elem):
            if not elem:
                return 0
            nonlocal res

            h_right = dfs(elem.right)
            h_left = dfs(elem.left)

            if abs(h_left - h_right) > 1:
                res = False

            return 1 + max(h_right, h_left) # returning the height of the whole subtree

        dfs(root)
        return res

