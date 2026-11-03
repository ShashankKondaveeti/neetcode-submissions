# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smallest = min(p.val,q.val)
        if root and (root.val > smallest and root.val < max(p.val,q.val)):
            return root 
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        if root.val > smallest:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)