class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        elems = {}

        def dfs(elem):
            if res:
                return

            elems[elem] = set()
            elems[elem].add(elem.val)

            if elem.left:
                dfs(elem.left)
                elems[elem] |= elems[elem.left]

            if elem.right:
                dfs(elem.right)
                elems[elem] |= elems[elem.right]

            if p.val in elems[elem] and q.val in elems[elem]:
                res.append(elem)

        dfs(root)
        return res[0]

