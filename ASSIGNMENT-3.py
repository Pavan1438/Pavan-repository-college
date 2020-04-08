class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
  
# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print("%d" %(root.data)) 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
  
  
""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
# Driver program to test above function 
root = Node(11) 
root.left = Node(12) 
root.right = Node(13) 
root.left.left = Node(14) 
root.left.right = Node(15)
root.left.left.left=Node(16)
root.right.right=Node(17) 
root.right.right.left=Node(18)
  
print("Level order traversal of binary tree is -")
printLevelOrder(root) 

'''
Output:
Level order traversal of binary tree is -
11
12
13
14
15
17
16
18
'''