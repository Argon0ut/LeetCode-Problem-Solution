from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def dfs(elem, arr):
            if not elem:
                return
            else:
                arr.append(',' + str(elem.val))

            if elem.left:
                dfs(elem.left, arr)
            else:
                arr.append('x')

            if elem.right:
                dfs(elem.right, arr)
            else:
                arr.append('x')

        arr1 = []
        dfs(subRoot, arr1)

        arr2 = []
        dfs(root, arr2)

        s1 = ''.join(arr1)
        s2 = ''.join(arr2)

        return s1 in s2

