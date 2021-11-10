from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    if tree1 is None or tree2 is None:
        if tree1 is None and tree2  is None:
            return True
        else:
            return False
        
    if tree1.data != tree2.data:
        return False
        
    count1 = len(tree1.children)
    count2 = len(tree2.children)
    
    if count1 != count2:
        return False
    
    if (count1==count2) and tree1.data == tree2.data:
        for i in range (count2):
            isIdentical(tree1.children[i],tree2.children[i])
            
        return True
    else:
        return False
    





def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')