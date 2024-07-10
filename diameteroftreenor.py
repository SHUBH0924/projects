class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if root is None:
        return 0

    p_diam = 1 + height(root.left) + height(root.right)
    lc_diam = diameter(root.left)
    rc_diam = diameter(root.right)

    return max(p_diam, max(lc_diam, rc_diam))


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

print("The diameter of whole Tree is: {}".format(diameter(root)))