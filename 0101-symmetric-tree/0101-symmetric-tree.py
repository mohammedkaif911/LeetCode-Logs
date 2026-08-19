# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left,right):
            if left is None and right is None:
                return True
                
            if left is None or right is None:
                return False

            if left.val != right.val:
                return False
            
            inside = symmetric(left.right,right.left)
            outside = symmetric(left.left,right.right)
            return inside and outside


        return symmetric(root.left,root.right)

        