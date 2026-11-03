# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            curr_node = stack.pop()

            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            if curr_node.right:
                stack.append(curr_node.right)
            
            if curr_node.left:
                stack.append(curr_node.left)
        return root 