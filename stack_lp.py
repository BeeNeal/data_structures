# stack DS from Lucid Programming Youtube

class Stack():

    def __init__(self):
        """Implements with list, b/c already has many chars of stack """

        self.items = []

    def push(self, new_item):
        """Puts new item on top of the stack. """

        self.items.append(new_item)

    def pop(self):
        """Removes item from top of stack and returns it """

        return self.items.pop()

    def peek(self):
        """Return top elem of the stack"""

        return self.items[-1]

    def is_empty(self):
        """Returns bool on if items are in list """

        return self.items == []

    def get_stack(self):
        """ """

        return self.items

s = Stack()
s.push('A')
s.push('B')
print(s.get_stack())
s.push('C')
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()
print(s.is_empty())
s.pop()
print(s.is_empty())
s.push('M')
print(s.peek())


