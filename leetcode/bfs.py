from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # bfs, basic implementation, not needing to track level
    def basic_bfs(root):
        result = []
        queue = deque([root])

        while queue:
            curr_node = queue.popleft()
            result.append(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return result
    
    # tracking level
    def level_order(root):
        if not root:
            return []
        
        result = []
        # initialize queue with array
        queue = deque([root])

        while queue:
            # nodes at current level
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                curr_node = queue.popleft()
                # unsure if .val or not
                curr_level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            result.append(curr_level)
        
        return result
        