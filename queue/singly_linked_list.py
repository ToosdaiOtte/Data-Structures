class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            # if self.head is None and self.tail is None
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None
        # list with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # list with +2 Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        #Consider the same three cases we used in remove_head()
        # 1. empty list
        if self.head is None:
            return None
        # 2. list with one element
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # 3. list with two or more elements
        else:
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            value = self.tail.get_value()
            cur_node.set_next(None)
            self.tail = cur_node
            self.length -= 1
            return value

    def contains(self, value):
        # 1. use a loop to iterate through the linked list 
        # 2. check if the value of the current node is the value we are searching for
        # 3. return True if we find it, False if we reach the end of the linked list
        cur_node = self.head
        while cur_node is not None:
        # return True if we find value
            if value == cur_node.get_value():
                return True
            cur_node = cur_node.next_node
        # return False if we reach end of LL
        return False

    # What we wrote together in the Guided Project...

    # def get_max(self):
        # iterate through all elements
        #cur_node = self.head
        #cur_max = self.head.get_value()
        #while cur_node is not None:
            #if cur_node.get_value() > cur_max:
                #cur_max = cur_node.get_value()
            #cur_node = cur_node.get_next()

    # A completed get_max() method...
    def get_max(self):
        # empty list
        if self.head is None:
            return None
        # non-empty list
        # iterate through all elements
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()

        return cur_max
    