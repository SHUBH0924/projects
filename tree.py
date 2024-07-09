class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def calcInorder(root):
 
    if root:
 
        # Recurring on left child
        calcInorder(root.left)
 
        # Printing data of node
        print(root.val, end=" "),
 
        # Recurring on right child
        calcInorder(root.right)
 
 
# A function to do postorder tree traversal
def calcPostorder(root):
 
    if root:
 
        # Recurring on left child
        calcPostorder(root.left)
 
        # Recurring on right child
        calcPostorder(root.right)
 
        # Printing data of node
        print(root.val, end=" "),
 
 
# A function to do preorder tree traversal
def calcPreorder(root):
 
    if root:
 
        # Printing data of node
        print(root.val, end=" "),
 
        # Recurring on left child
        calcPreorder(root.left)
 
        # Recurring on right child
        calcPreorder(root.right)
 
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Preorder: ")
calcPreorder(root)
 
print ("\nInorder: ")
calcInorder(root)
 
print ("\nPostorder: ")
calcPostorder(root)