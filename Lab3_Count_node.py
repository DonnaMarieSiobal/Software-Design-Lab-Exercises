class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def left_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.left
    return ht

def right_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.right
    return ht

def TotalNodes(root):
    # Base case
    if (root == None):
        return 0

    lh = left_height(root)
    rh = right_height(root)

    if (lh == rh):
        return (1 << lh) - 1

    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


# Driver code
root = node(20)
root.left = node(15)
root.right = node(25)
root.left.left = node(10)
root.left.right = node(19)
root.right.left = node(21)
root.right.right = node(70)


print("The total number of node in Binary Tree is:", TotalNodes(root))
