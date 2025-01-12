class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def intro_dfs(self, root):
        if root is None:
            return -9998999
        
        if root.left is None and root.right:
            return True


1 4 6 