class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root


root = insert(None, 20)
insert(root, 15)
insert(root, 19)
insert(root, 10)
insert(root, 25)
insert(root, 21)
insert(root, 70)

a1 = root
a2 = a1.leftChild
a3 = a1.rightChild
a4 = a2.leftChild
a5 = a2.rightChild
a6 = a3.leftChild
a7 = a3.rightChild

print("Root Node is:", a1.data)
print("left child of node is:", a1.leftChild.data)
print("right child of node is:", a1.rightChild.data)
print("\nNode is:", a2.data)
print("left child of node is:", a2.leftChild.data)
print("right child of node is:", a2.rightChild.data)
print("\nNode is:", a3.data)
print("left child of node is:", a3.leftChild.data)
print("right child of node is:", a3.rightChild.data)

