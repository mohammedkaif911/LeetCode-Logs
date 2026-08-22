# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = 0
        def check(node, level):
            if node is None:
                return
            if level == len(result):        
                result.append([])          
            result[level].append(node.val)  
            check(node.left, level + 1)
            check(node.right, level + 1)
        check(root,level)
        return result
        