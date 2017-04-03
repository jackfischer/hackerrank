"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head: Node) -> bool:
    current = head
    slow = current
    fast = current
    
    while True:
        #Move fast ahead twice or return if end
        if fast.next is None:
            return False
        fast = fast.next
        if fast.next is None:
            return False
        fast = fast.next
        #Slow won't hit None
        slow = slow.next
        #Has to either finish or touch the same node
        if fast == slow:
            return True
    
