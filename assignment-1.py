# Python program to create Root Node 
class Tree(object): 
    def __init__(self): 
        self.left = None 
        self.right = None 
        self.data = None 
        
        
root = Tree() 
root.data ="A" 
root.left = Tree() 
root.left.data = "B" 
root.right = Tree() 
root.right.data = "C"
root.left.left=Tree()
root.left.left.data= "D"
root.left.right=Tree()
root.left.right.data="E"
root.right.left = Tree()
root.right.left.data="F"
root.right.right = Tree()
root.right.right.data="G"



print(root.data)
print(root.left.data) 
print(root.right.data) 
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)

'''
Output:
A
B
C
D
E
F
G
'''