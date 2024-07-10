class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def print_left_view_helper(root):
    max_level_visited = [0]
    print_left_view(root, max_level_visited, 1)


def print_left_view(node, max_level_visited, curr_level):
    if node is None:
        return

    if max_level_visited[0] < curr_level:
        print(node.data, end=" ")
        max_level_visited[0] = curr_level

    print_left_view(node.left, max_level_visited, curr_level + 1)
    print_left_view(node.right, max_level_visited, curr_level + 1)


# Driver code
root = Node(20)
root.left = Node(70)
root.right = Node(90)
root.left.left = Node(30)
root.left.right = Node(40)
root.right.right = Node(70)

print_left_view_helper(root)