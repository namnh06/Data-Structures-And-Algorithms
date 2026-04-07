import unittest
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


class TestTreeNode(unittest.TestCase):
    def test_default_children_are_none(self) -> None:
        node = TreeNode(1)

        self.assertEqual(node.val, 1)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_explicit_children_are_assigned(self) -> None:
        left = TreeNode(2)
        right = TreeNode(3)
        node = TreeNode(1, left, right)

        self.assertEqual(node.val, 1)
        self.assertIs(node.left, left)
        self.assertIs(node.right, right)
        assert node.left is not None
        assert node.right is not None
        self.assertEqual(node.left.val, 2)
        self.assertEqual(node.right.val, 3)

    def test_leetcode_example_tree_structure(self) -> None:
        # root = [4,2,7,1,3,6,9]
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )

        self.assertEqual(root.val, 4)
        assert root.left is not None
        assert root.right is not None
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 7)

        assert root.left.left is not None
        assert root.left.right is not None
        assert root.right.left is not None
        assert root.right.right is not None
        self.assertEqual(root.left.left.val, 1)
        self.assertEqual(root.left.right.val, 3)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 9)
        
    def test_leetcode_example_testcase_3(self) -> None:
        solution = Solution()
        root: Optional[TreeNode] = None

        self.assertIsNone(solution.invertTree(root))    
        
    def test_leetcode_example_testcase_2(self) -> None:
        solution = Solution()
        root: Optional[TreeNode] = TreeNode(
            2, TreeNode(1), TreeNode(3)
        )
        
        inverted_root: Optional[TreeNode] = solution.invertTree(root)
        
        assert inverted_root is not None
        self.assertEqual(inverted_root.val, 2)
        assert inverted_root.left is not None
        assert inverted_root.right is not None
        self.assertEqual(inverted_root.left.val, 3)
        self.assertEqual(inverted_root.left.val, 1)

    def test_leetcode_example_testcase_1(self) -> None:
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )

        inverted_root = solution.invertTree(root)

        assert inverted_root is not None
        self.assertEqual(inverted_root.val, 4)
        assert inverted_root.left is not None
        assert inverted_root.right is not None
        self.assertEqual(inverted_root.left.val, 7)
        self.assertEqual(inverted_root.right.val, 2)

        assert inverted_root.left.left is not None
        assert inverted_root.left.right is not None
        assert inverted_root.right.left is not None
        assert inverted_root.right.right is not None
        self.assertEqual(inverted_root.left.left.val, 9)
        self.assertEqual(inverted_root.left.right.val, 6)
        self.assertEqual(inverted_root.right.left.val, 3)
        self.assertEqual(inverted_root.right.right.val, 1)


if __name__ == "__main__":
    unittest.main()
