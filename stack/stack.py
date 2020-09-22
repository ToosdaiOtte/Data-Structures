"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

    - Linked list doesn't have the methods that are available to use with arrays such as len(), append(), and pop()
"""
# import LinkedList class
from singly_linked_list import LinkedList

# stack with array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)


    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()        

# stack with linkedlist
class LL:
    def __init__(self):
        self.size = 0
        # assigning storage to linkedlist
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head
        self.size += 1

    def pop(self):
        # empty list
        if self.size == 0:
            return None
        # list with elements
        else:
            return self.storage.remove_head()