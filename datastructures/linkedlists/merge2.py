"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def append(root, data):
    root.next = Node(data=data)
    return root.next


def MergeLists(headA, headB):
    root = Node()
    temp = root
    while True:
        if headA is not None and headB is not None:
            if headA.data <= headB.data:
                temp = append(temp, headA.data)
                headA = headA.next
            else:
                temp = append(temp, headB.data)
                headB = headB.next
        elif headA is not None:
                temp.next = headA
                break
        elif headB is not None:
                temp.next = headB
                break

    return root.next
            