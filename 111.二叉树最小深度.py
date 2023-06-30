from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        if root.left == None :
            return 1 + self.minDepth(root.right)

        elif root.right == None:
            return 1 + self.minDepth(root.left)
        
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ == "__main__":

    e = TreeNode(0)
    d = TreeNode(0, left =e)
    c = TreeNode(0, left =d)
    b = TreeNode(0, left =c)
    a = TreeNode(0,left=b)

    solution = Solution()
    
    res = solution.minDepth(a)
    print(res)

