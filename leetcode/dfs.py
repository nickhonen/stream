class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def recursive_dfs(self, root):
        print()

    def iterative_dfs(self, root):
        if root is None:
            return []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                print(node)
                stack.append(node.)

        return stack


    def invert_tree(self, root: Optional[TreeNode]):
        if root is None:
            return []

        result = []
        stack = [[root]]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
            print(node)
        return stack