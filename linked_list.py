class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        # need to traverse and set prev to next but still move to next node
        # initialize previous to none
        prev = None
        # while there is a head, traverse to next, set current.next to previous, set previous to current
        while self.head:
            current = self.head
            self.head = self.head.next
            current.next = prev
            prev = current
        self.head = prev

    def reverseRecursively(self, head, prev=None):
        if not head:
            return prev

            curr, head.next = head.next, prev
            return self.reverseRecursively(curr, head)

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


ll = LinkedList()
ll.append('Omar')
ll.append('likes')
ll.append('Brittany')
ll.printList()
ll.reverseRecursively(ll.head)
ll.printList()