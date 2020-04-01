# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#top-bottom
class Solution:
    def __init__(self):
        self.depth=0
        
    def maxDepth(self, root: TreeNode) -> int:
        def topbottom(root,level):
            if root is None:
                return
            if(root.left is None and root.right is None):
                self.depth=max(self.depth,level)
            topbottom(root.left,level+1)
            topbottom(root.right,level+1)
        
        topbottom(root,1)
        return self.depth


#bottom-up
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        else:
            return 0
