from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = {}

        def dfs(elem, counter):
            if not elem:
                return

            if counter not in levels:
                levels[counter] = [elem.val]
            else:
                levels[counter].append(elem.val)

            counter += 1

            if not elem.right and not elem.left:
                return

            if elem.left:
                dfs(elem.left, counter)
            if elem.right:
                dfs(elem.right, counter)

        dfs(root, 0)

        res = []
        for i in levels:
            res.append(levels[i][-1])

        return res