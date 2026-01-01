class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        #pre-order traversal

        res = 0

        def dfs(elem, arr):
            if not elem:
                return

            nonlocal res

            if not arr or elem.val >= max(arr):
                res += 1

            arr.append(elem.val)

            if elem.left:
                dfs(elem.left, arr)
                arr.pop()

            if elem.right:
                dfs(elem.right, arr)
                arr.pop()
        dfs(root, [])

        return res
