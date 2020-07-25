# Definition for a binary tree node
# Assuming the height of the leaves is zero
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Height_of_Binary_tree(root):
    if root==None:
        return -1
    else:
        lh = Height_of_Binary_tree(root.left)
        rh = Height_of_Binary_tree(root.right)
        if (lh>rh):
            return lh + 1
        else:
            return rh + 1

# Tree construction
Root = Node(10)
Root.left = Node(5)
Root.right = Node(40)
Root.left.left = Node(1)
Root.left.right = Node(7)
Root.right.left = Node(50)
Root.right.left.right = Node(55)

print(Height_of_Binary_tree(Root))