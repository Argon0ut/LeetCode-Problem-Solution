from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []

        def dfs(elem):
            if not elem:
                return

            nonlocal arr

            if elem.left:
                dfs(elem.left)

            arr.append(elem.val)

            if elem.right:
                dfs(elem.right)

        dfs(root)

        return arr