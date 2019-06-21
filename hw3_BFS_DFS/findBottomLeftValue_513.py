# 513. Find Bottom Left Tree Value

# Runtime: 48 ms
# Memory Usage: 16.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.leftlevel = 0
        self.leftvar = None

        self.dfs(root, 1)

        return self.leftvar

    def dfs(self, root, level):
        if root.left == None and root.right == None:
            if level > self.leftlevel:
                self.leftlevel = level
                self.leftvar = root.val
        else:
            if root.left:
                self.dfs(root.left, level+1)
            if root.right:
                self.dfs(root.right, level+1)
