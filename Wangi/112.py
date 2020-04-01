# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursion
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum-=root.val
        if not root.left and not root.right:
            if(sum==0):
                return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

#iterative
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack=[(root,sum-root.val), ]
        while stack:
            root,sum=stack.pop()
            if not root.left and not root.right and sum==0:
                return True
            if root.left:
                stack.append((root.left,sum-root.left.val))
            if root.right:
                stack.append((root.right,sum-root.right.val))
        return False