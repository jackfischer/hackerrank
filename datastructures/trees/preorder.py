"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    result = list()
    stack = list()
    stack.append(root)
    while len(stack) is not 0:
        temp = stack.pop()
        if temp.right is not None:
            stack.append(temp.right)
        if temp.left is not None:
            stack.append(temp.left)
        result.append(str(temp.data))
        
    print(' '.join(result))
        
        