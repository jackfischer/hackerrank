"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def doParent(parent, result):
    """Left, right, parent"""
    if parent.left is not None:
        doParent(parent.left, result)
    if parent.right is not None:
        doParent(parent.right, result)
    result.append(parent.data)
    
    return result
    
    
def postOrder(root):
    #Write your code here
    result = list()
    
    result = doParent(root, result)
    result = [str(i) for i in result]
    print(' '.join(result))
        
        