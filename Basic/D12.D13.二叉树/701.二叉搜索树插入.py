from typing import Optional
from binarytree import tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     self

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:

        if root == None:
            return TreeNode(val, None)


        if root.val > val:
            print('left', root.val)
            root.left = self.insertIntoBST(root.left, val)

        # root.val > val:
        else:
            print('right', root.val)
            root.right = self.insertIntoBST(root.right, val)

        return root




  #   3
  #  / \
  # 1  20
  #   /  \
  #  15   25
  #
tree1 = TreeNode(val = 15)
tree2 = TreeNode(val = 25)
tree3 = TreeNode(val = 20, left = tree1, right=tree2)
tree4 = TreeNode(val = 1)
tree5 = TreeNode(val = 3, left = tree4,right = tree3)





a = Solution()

root = a.insertIntoBST(tree5, 100)

root.right.right.val



help(tree)








# try to use binarytree to build a tree


