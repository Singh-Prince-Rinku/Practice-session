class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return bool(root.val)
        a = self.evaluateTree(root.left)
        b = self.evaluateTree(root.right)
        return a or b if root.val == 2 else a and b