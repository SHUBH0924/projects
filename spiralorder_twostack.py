class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def spiral_order(root):
    if root is None:
        return

    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) != 0 or len(stack2) != 0:

        while len(stack1) != 0:
            temp = stack1.pop()
            print(temp.data, end=" ")

            if temp.left is not None:
                stack2.append(temp.left)

            if temp.right is not None:
                stack2.append(temp.right)
        print()

        while len(stack2) != 0:
            temp = stack2.pop()
            print(temp.data, end=" ")

            if temp.right is not None:
                stack1.append(temp.right)

            if temp.left is not None:
                stack1.append(temp.left)

        print()


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)

spiral_order(root)