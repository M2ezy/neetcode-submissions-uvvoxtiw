# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return [True, 0]

            left = height(node.left)
            right = height(node.right)

            curheight = max(left[1], right[1]) + 1
            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            
            return [balanced, curheight]
        res = height(root)
        return res[0]