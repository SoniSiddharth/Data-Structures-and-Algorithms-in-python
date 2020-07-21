# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class diameterOfBinaryTree:

    def __init__(self):
        None
    
    def diamter(self, item):
        self.ans=0

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            
            self.ans = max(self.ans, L+R+1)
            return max(L,R)+1

        depth(root)
        return self.ans

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
root.right.left = TreeNode(6)

ans = diameterOfBinaryTree()
print(ans.diamter(root))