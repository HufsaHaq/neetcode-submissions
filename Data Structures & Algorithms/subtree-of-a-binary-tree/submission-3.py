# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to call the helper function same tree
        if not subRoot : return True
        if not root: return False

        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self, root: Optional[TreeNode], subTree: Optional[TreeNode]) -> bool:
        if not root and not subTree:
            return True # true because theyre both empty trees

        if root and subTree and root.val == subTree.val:
            return self.sameTree(root.left,subTree.left) and self.sameTree(root.right, subTree.right)

        return False