from typing import Optional

# This problem's aim is to find the depth of the tree, or in other words the height of the tree
# it is essential to know this pattern because it is widely used in other problems too.

# Approach --> we set a function dfs which gets TreeNode and counter(current height of the element) as arguments
# We then iterate through the nodes to get the maximum height comparing it with global variable res

#Complexities:
# Time --> O(n) --> it is visiting each node
# Space --> O(1) --> no extra space is being allocated

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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
