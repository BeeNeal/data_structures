        

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, new_val):
        """Insert new node as head (in first position)."""

        if not self.head:
            self.head = ListNode(new_val)
        else:
            new_node = ListNode(new_val)
            new_node.next = self.head
            self.head = new_node
    
    def printNodes(self):
        """print out node values of linked list."""

        current = self.head
        while current:
            print(current.val)
            current = current.next

    def reverse(self):
        """Reverse linked list in place."""

        prev = None
        while self.head:
            current = self.head
            self.head = self.head.next
            current.next = prev
            prev = current
        self.head = prev




def addTwoNumbers(self, ll1, ll2):
    """Add 2 integers in linked list format without ll integer for output."""

    # with a normal list, could reverse and work backwards, and check for overflow (9 + 1)
    # but with a linked list, need to iterate through each node to arrive at
    # the end. Also, if working from the front, if have ll of uneven lengths, 
    # place value will be messed up. So if must work from back, implement 
    # reverse ll method, OR make into dll then walk backwards through both dlls
    #  and insert added nodes to first position (as head), making a check for the overflow 

    ll1.reverse()
    ll2.reverse()
    output_ll = LinkedList()
    overflow = False
    while ll1.head and ll2.head:
        combined_val = ll1.head.val + ll2.head.val
        if combined_val > 9:
            overflow = True
            output_ll.insert(10 - combined_val)
        elif overflow == True:
            combined_val += 1
            if combined_val < 10:
                output_ll.insert(combined_val)
            else:
                output_ll.insert(0)
                # overflow still True
        else:
            output_ll.insert(combined_val)


def add(ll1, ll2):
    ll1.reverse()
    ll2.reverse()
    summed_int = LinkedList()
    overflow = False
    while ll1.head and ll2.head:
        combined_val = ll1.head.val + ll2.head.val
        if combined_val < 10 and not overflow:
            summed_int.insert(combined_val)
            overflow = False
        elif combined_val >= 10 and not overflow:
            overflow = True
            summed_int.insert(10 - combined_val)
        elif combined_val < 10 and overflow:
            overflow = True
            combined_val += 1
            summed_int.insert(10 - combined_val)
        # else:  # combined_val >= 10 and overflow
        #     overflow = True
        #     summed_int.insert(10 - combined_val)
        ll1.head = ll1.head.next
        ll2.head = ll2.head.next

        #  take care of remaining integers in case linked lists are uneven
        while ll1.head:
            summed_int.insert(ll1.head.val)
            ll1.head = ll1.head.next
        while ll2.head:
            summed_int.insert(ll2.head.val)
            ll2.head = ll2.head.next


    return summed_int
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
ll1 = LinkedList()
ll1.insert(3)
ll1.insert(4)    
ll1.insert(2)    
ll1.printNodes()

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
ll2 = LinkedList()    
ll2.insert(4)
ll2.insert(6)
ll2.insert(5)
ll2.printNodes()

x = add(ll1, ll2)
x.printNodes()