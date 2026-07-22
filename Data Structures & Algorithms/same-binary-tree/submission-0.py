# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both empty
        if not p and not q:
            return True
        
        # Case 2: one empty, one not
        if not p or not q:
            return False
        
        # Case 3: values differ
        if p.val != q.val:
            return False
        
        # Case 4: recursively check subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def depth(self,p):
        try:
            if p.val == []:
                return 0
        except:
            return 0

        count1 = 0
        count2 = 0
        total = 0

        if p.left:
            count1 += self.depth(p.left)

        if p.right:
            count2 += self.depth(p.right)

        if p.val:
            total +=1

        return total + max(count1,count2)

