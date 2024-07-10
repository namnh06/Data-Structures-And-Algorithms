import sys
import os
from typing import Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Others')))

from BinaryTree import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    root = None
    assert Solution().maxDepth(root) == 0, "Test case 1 failed"

    root = TreeNode(1)
    assert Solution().maxDepth(root) == 1, "Test case 2 failed"

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().maxDepth(root) == 2, "Test case 3 failed"

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().maxDepth(root) == 3, "Test case 4 failed"

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().maxDepth(root) == 3, "Test case 5 failed"

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3, "Test case 6 failed"

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert Solution().maxDepth(root) == 4, "Test case 7 failed"
    
    print("All test cases passed.")