# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,lower,upper):
            if node is None:
                return True
            if not(lower<node.val<upper):
                return False
            
            rightValidate = validate(node.right,node.val,upper)
            leftValidate = validate(node.left,lower,node.val)

            return rightValidate and leftValidate
        
        return validate(root,float("-inf"),float("+inf"))

        