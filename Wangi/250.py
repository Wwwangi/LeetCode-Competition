# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res=0
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def unitree(tree):
            if not tree:
                return
            if not tree.left and not tree.right:
                self.res+=1
                return True
            temp=True
            if tree.left:
                temp= unitree(tree.left) and tree.left.val==tree.val
            if tree.right:
                temp=unitree(tree.right) and temp and tree.right.val==tree.val
            if(temp==True):
                print(tree)
                self.res+=1
                return True
            return False
        
        unitree(root)
        return self.res