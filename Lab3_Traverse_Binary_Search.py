class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "-->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "-->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "-->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(20)
root.right.right = Node(70)

print("Inorder traversal")
inorder(root)

print("\n\nPreorder traversal")
preorder(root)

print("\n\nPostorder traversal")
postorder(root)

