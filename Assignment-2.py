class Node: 
    def __init__(self,key): 
        self.left = None 
        self.right = None 
        self.val = key   # A function to do inorder tree traversal 
def printInorder(root):  
    if root:  # First recur on left child 
        printInorder(root.left)  # then print the data of node      
        print(root.val)   # now recur on right child 
        printInorder(root.right) 
def printPostorder(root):   
    if root: # First recur on left child
        printPostorder(root.left)  # the recur on right child 
        printPostorder(root.right) # now print the data of node 
        print(root.val) 
def printPreorder(root):
    if root:  # First print the data of node 
        print(root.val)  # Then recur on left child 
        printPreorder(root.left)  # Finally recur on right child 
        printPreorder(root.right)



root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
root.left.left.left= Node(6)
root.left.left.right = Node(7)
root.right.left=Node(8)
root.right.right = Node(9)
print("Preorder traversal of binary tree is")
printPreorder(root) 
  
print("\nInorder traversal of binary tree is")
printInorder(root) 
  
print("\nPostorder traversal of binary tree is")
printPostorder(root) 


'''
Output:
Preorder traversal of binary tree is
1
2
4
6
7
5
3
8
9

Inorder traversal of binary tree is
6
4
7
2
5
1
8
3
9

Postorder traversal of binary tree is
6
7
4
5
2
8
9
3
1    '''