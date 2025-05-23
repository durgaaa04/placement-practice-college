class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def Inorder(root):
    if root!=None:
        Inorder(root.left)
        print(str(root.key), end = " ")
        Inorder(root.right)

def Preorder(root):
    if root!=None:
        print(str(root.key), end = " ")
        Preorder(root.left)
        Postorder(root.right)

def Postorder(root):
    if root!=None:
        Postorder(root.left)
        Postorder(root.right)
        print(str(root.key), end = " ")
    
    #insert
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def inorder_succ(root):
    curr = root.right
    while curr.left  != None:
        curr = curr.left
    print(curr.key)
    return curr

def inorder_pred(root): 
    curr = root.left
    while curr.right != None:
        curr = curr.right
    print(curr.key)

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = inorder_succ(root.right) 
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
    
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("inorder traversal:", end = " ")
Inorder(root)
print("\npreorder traversal:", end = " ")
Preorder(root)
print("\npostorder traversal:", end = " ")
Postorder(root)
print("\ninorder succesor:", end = " ")
inorder_succ(root)
print("\ninorder predeccesor:", end = " ")
inorder_pred(root)
print("\ndeleting node:", end = " ")
deleteNode(root, 3)