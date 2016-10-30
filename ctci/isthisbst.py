""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check_binary_search_tree_(node, floorIn=0, ceilingIn=10000):
    """
    Check if children data obey BST property
    Check if both children are BSTs recursively 
    """
    if node is None:
        return True
    
    """
    if node.data > floor:
        floor = node.data
    if node.data < ceiling:
        ceiling = node.data
    """
    
    if node.left is not None and (node.left.data >= node.data or node.left.data <= floorIn):
        return False
    if node.right is not None and (node.right.data <= node.data or node.right.data >= ceilingIn):
        return False
    
    
    if not check_binary_search_tree_(node.left, floorIn, node.data):
        return False
    if not check_binary_search_tree_(node.right, node.data, ceilingIn):
        return False
    
    
    return True

