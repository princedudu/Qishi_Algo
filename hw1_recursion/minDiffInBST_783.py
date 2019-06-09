import sys
#leetcode 783. Minimum Distance Between BST Nodes
#inorder travarse

#performance
#Runtime: 32 ms, faster than 97.26% of Python3 online submissions for Minimum Distance Between BST Nodes.
#Memory Usage: 13.2 MB, less than 59.09% of Python3 online submissions for Minimum Distance Between BST Nodes.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    use inorder iterative traversal to compare the node value
    """
    def minDiffInBST(self, root: TreeNode) -> int:
        minDiff = sys.maxsize
        q = []
        pre = None
        while root or q:
            if root:
                q.append(root)
                root = root.left
            else:
                node = q.pop()
                if pre:
                    minDiff = min(minDiff, node.val - pre)
                pre = node.val
                root = node.right
        return minDiff
