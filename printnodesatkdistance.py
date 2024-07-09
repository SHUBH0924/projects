class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def printKDistance(node, k):
    
    if node is None:
        return 
    elif k == 0:
        print (node.data)
    else:
        printKDistance(node.left, k-1)
        printKDistance(node.right, k-1)

            
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

k = 2

print ("Items at distance {} are : ".format(k))
printKDistance(root, k)