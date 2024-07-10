class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def spiral_order_helper(root):
    left_to_right = True
    spiral_order(root, left_to_right)


def spiral_order(root, left_to_right):
    if root is None:
        return

    queue = []
    stack = []
    queue.append(root)

    while len(queue) > 0:

        n = len(queue)
        for i in range(0,n):
            temp = queue[0]
            queue.pop(0)

            if left_to_right:
                print(temp.data, end=" ")
            else:
                stack.append(temp)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

        if left_to_right == False:
            while len(stack) >0:
                print(stack.pop().data, end=" ")

        print()
        left_to_right = not left_to_right


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

spiral_order_helper(root)