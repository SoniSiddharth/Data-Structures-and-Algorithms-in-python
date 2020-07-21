class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructTree(pre, low, high, size):
    global preInd
    if( preInd >= size or low > high): 
        return None
    
    root = TreeNode(pre[preInd]) 
    preInd+=1
    if low == high : 
        return root 
    i = low
    while(i<high+1): 
        if (pre[i] > root.val): 
            break
        i+=1
    root.left = constructTree(pre, preInd, i-1 , size)
    root.right = constructTree(pre, i, high, size)
    return root

pre = [10,5,1,7,20,40]
low = 0
high = len(pre) - 1
size = k=len(pre)
preInd = 0

ans = constructTree(pre, low, high, size)

print(ans.left.val)
print(ans.right.val)
print(ans.left.right.val)
