class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BST_from_postorder(post, low, high, size):
    global postInd
    if (postInd>=size or low>high):
        return None
    root = Node(post[high])
    postInd-=1

    if low==high:
        return root
    i = low
    x = post[high]
    while(i<high+1):
        if post[i]>x:
            break
        i+=1
    root.right = BST_from_postorder(post, i, postInd, size)
    root.left = BST_from_postorder(post, low, i-1, size)
    return root

post = [1, 7, 5, 50, 40, 10]  # postorder array
low = 0
high = len(post) - 1
size = len(post)
postInd = len(post) - 1

# function call
ans = BST_from_postorder(post, low, high, size)

print(ans.data)
print(ans.left.data)
print(ans.right.data)
print(ans.left.right.data)