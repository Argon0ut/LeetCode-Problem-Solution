from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False

        res = True

        def dfs(elem1, elem2):
            nonlocal res

            if not res:
                return

            if not elem1 and not elem2:
                res = False
                return

            if elem1.val != elem2.val:
                res = False
                return

            if (elem1.left and elem2.left) or (not elem1.left and not elem2.left):
                dfs(elem1.left, elem2.left)
            else:
                res = False
                return

            if (elem1.right and elem2.right) or (not elem1.right and not elem2.right):
                dfs(elem1.right, elem2.right)
            else:
                res = False
                return

        dfs(p, q)
        return res


