from typing import Optional, List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = {}

        def dfs(elem, counter):
            if not elem:
                return

            if counter not in levels:
                levels[counter] = []
            levels[counter].append(elem.val)

            counter += 1

            if not elem.left and not elem.right:
                return

            if elem.left:
                dfs(elem.left, counter)
            if elem.right:
                dfs(elem.right, counter)

        dfs(root, 0)

        res = []
        for i in levels:
            res.append(levels[i])

        return res
