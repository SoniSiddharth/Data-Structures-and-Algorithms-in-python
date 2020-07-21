class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def preorder(root):
    if root:
        print(root.data)        
        preorder(root.left_child)
        preorder(root.right_child)

def postorder(root):
    if root:        
        postorder(root.left_child)
        postorder(root.right_child)
        print(root.data)

def inorder(root):
    if root:        
        inorder(root.left_child)
        print(root.data)
        inorder(root.right_child)

if __name__ == "__main__":
    
    root = Node(5)
    root.left_child = Node(2)
    root.right_child = Node(10)
    preorder(root)
    postorder(root)
    inorder(root)

