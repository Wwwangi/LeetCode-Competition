# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[root, ]
        res=[]
        while stack:
            root=stack.pop()
            if root is not None:
                if(root.right is not None):
                    stack.append(root.right)
                if(root.left is None and root.right is None):
                    res.append(root.val)
                else:
                    stack.append(TreeNode(root.val))
                if(root.left is not None):
                    stack.append(root.left)
        return res
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root,res):
            if not root:
                return
            preorder(root.left,res)
            res.append(root.val)
            preorder(root.right,res)
            return res
        
        res=[]
        res=preorder(root,res)
        return res
            