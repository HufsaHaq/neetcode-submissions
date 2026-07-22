# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count1 = 0
        count2 = 0
        total = 0

        try:
            if root.val == []:
                return 0
        except:
            return 0

        if root.left:
            count1 += self.maxDepth(root.left)

        if root.right:
            count2 += self.maxDepth(root.right)

        total +=1

        return total + max(count1,count2)
