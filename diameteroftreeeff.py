class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

max_diam = 0

def height(root):
    if root is None:
        return 0

    lc_height = height(root.left)
    rc_height = height(root.right)
    
    global max_diam
    max_diam = max(max_diam, 1 + lc_height + rc_height)

    return 1 + max(lc_height, rc_height)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.right = Node(8)
root.left.left.left.left = Node(9)
root.left.right.right.right = Node(10)

print("The height of root node is: {}".format(height(root)))
print("The diameter of Tree is: {}".format(max_diam, 0))