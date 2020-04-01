# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(tree1,tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            return tree1.val==tree2.val and compare(tree1.left,tree2.right) and compare(tree1.right,tree2.left)
        
        return compare(root,root)

#iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue=collections.deque()
        queue.append(root)
        queue.append(root)
        while queue:
            tree1=queue.pop()
            tree2=queue.pop()
            if not tree1 and not tree2:
                continue
            if not tree1 or not tree2:
                return False
            if tree1.val!=tree2.val:
                return False
            queue.append(tree1.left)
            queue.append(tree2.right)
            queue.append(tree1.right)
            queue.append(tree2.left)
        return True