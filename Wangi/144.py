# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[root, ]
        res=[]
        while stack:
            print(stack)
            root=stack.pop()
            if root is not None:
                res.append(root.val)
                if(root.right is not None):
                    stack.append(root.right)
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root,res):
            if not root:
                return
            res.append(root.val)
            preorder(root.left,res)
            preorder(root.right,res)
            return res
        
        res=[]
        res=preorder(root,res)
        return res
            