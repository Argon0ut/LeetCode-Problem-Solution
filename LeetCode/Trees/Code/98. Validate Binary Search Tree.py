from typing import Optional, List
class TreeNode:
     def __init__(self, val = 0, left = None, right = None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root:Optional[TreeNode]) -> bool:
        arr = []

        def dfs(elem, arr):
            if not elem:
                return

            if elem.left:
                dfs(elem.left, arr)

            arr.append(elem.val)

            if elem.right:
                dfs(elem.right, arr)

        dfs(root, arr)

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False

        return True
