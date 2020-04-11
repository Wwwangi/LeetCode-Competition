# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter=1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def postorder(root):
            if not root:
                return 0
            left=postorder(root.left)
            right=postorder(root.right)
            self.diameter=max(self.diameter,left+right+1)
            return max(left,right)+1
        postorder(root)
        return self.diameter-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#我自己的版本
class Solution:
    def __init__(self):
        self.diameter=0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def postorder(root):
            left=0
            right=0
            if not root.left and not root.right:
                return 1
            if root.left:
                left=postorder(root.left)
            if root.right:
                right=postorder(root.right)
            self.diameter=max(self.diameter,left+right)
            return max(left,right)+1
        postorder(root)
        return self.diameter