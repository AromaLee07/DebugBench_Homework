from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        postorder_idx = len(postorder) - 1

        def treeHelper(left, right):
            nonlocal postorder_idx
            if left > right:
                return None

            node_val = postorder[postorder_idx]
            root = TreeNode(node_val)  # 这里缺少括号，应改为TreeNode(node_val)
            postorder_idx -= 1

            inorder_index = inorder_map[node_val]

            root.right = treeHelper(inorder_index + 1, right)  # 这里左右子树构建顺序有误，应先构建右子树
            root.left = treeHelper(left, inorder_index - 1)

            return root

        return treeHelper(0, len(inorder) - 1)
if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

#    "examples": [
#             "Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]\nOutput: [3,9,20,null,null,15,7]",
#             "Input: inorder = [-1], postorder = [-1]\nOutput: [-1]"
#         ],

    # nums = [2,3,5]
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    tree_root = solution.buildTree(inorder, postorder)


    def print_tree(node):
        if not node:
            return "None"
        return f"{node.val}, left: ({print_tree(node.left)}), right: ({print_tree(node.right)})"

    print("Constructed Binary Tree:", print_tree(tree_root))
