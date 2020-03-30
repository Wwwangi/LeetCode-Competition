# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        
        if root is None:
            return res
        
        def levels(root,level):
            if(len(res)==level):
                res.append([])
            res[level].append(root.val)
            if(root.left):
                levels(root.left,level+1)
            if(root.right):
                levels(root.right,level+1)
        
        levels(root,0)
        return res
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        
        if root is None:
            return res
        
        queue=collections.deque([root, ])
        level=0
        while queue:
            res.append([])
            NumOfNodes=len(queue)
            for i in range(NumOfNodes):
                temp=queue.popleft()
                res[level].append(temp.val)
                if(temp.left):
                    queue.append(temp.left)
                if(temp.right):
                    queue.append(temp.right)
            level+=1
        return res
            