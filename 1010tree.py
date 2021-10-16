def preorder(headnode):
    if headnode == ".":
        return
    
    print(headnode,end="")
    preorder(tree[headnode][0])
    preorder(tree[headnode][1])

def inorder(headnode):
    if headnode == ".":
        return
    
    inorder(tree[headnode][0])
    print(headnode,end="")
    inorder(tree[headnode][1])
    
def postorder(headnode):
    if headnode == ".":
        return
    
    postorder(tree[headnode][0])
    postorder(tree[headnode][1])
    print(headnode,end="")  

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left,right)

preorder("A")
print()
inorder("A")
print()
postorder("A")