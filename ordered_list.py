#Arman Rafian
#Section 7

class Node:
    ''' impliments a node item that will be the unit for OrderedList '''
    def __init__(self, data):
        self.data = data # data is a float representing a numeric value that the node holds
        self.next = None # next is an adress pointing to the next node in OrderedList
        self.prev = None
        
    def __repr__(self):
        return str(self.data)
        
class OrderedList:
    ''' impliments an ordered doubly linked list '''
    def __init__(self):
        self.head = None # head is a node represening the first node in the list
        self.num_nodes = 0 # self.num_nodes is a int representing the number of nodes (items) in the list
        self.tail = None # tail is a node reperesenting the last node int the list
        
    def __repr__(self):
        node_list = []
        trav = self.head
        while trav is not None:
            node_list.append(trav.data)
            trav = trav.next
        return str(node_list)
        
    # OrderedList, float ->
    def add(self, item):
        ''' adds an item to the list in its correct spot, assume that the item is not already in list '''
        current = self.head
        prev = None
        while (current is not None):
            if (current.data > item):
                break
            prev = current
            current = current.next
        # must be first addition
        if (prev is None):
            new_node = Node(item)
            # assign forwad connection
            new_node.next = current
            # by definition backwards must be None
            new_node.prev = None
            # new node is now first node in list
            self.head = new_node
            # if this is first node assign tail here
            if (self.num_nodes == 0):
                self.tail = new_node
            else:
                current.prev = new_node
        # must be last addition
        elif (current is None):
            new_node = Node(item)
            # assign foreward connection
            new_node.next = current
            # assign backwards connection
            new_node.prev = prev
            # asisign previous's forwards
            prev.next = new_node
            # new tail
            self.tail = new_node
        # must be middle addition
        else:
            new_node = Node(item)
            # assign foreward connection
            new_node.next = current
            # assign backwards connection
            new_node.prev = prev
            # assign next's backwards
            current.prev = new_node
            # asisign previous's forwards
            prev.next = new_node
            
        # want to increment it either way
        self.num_nodes += 1
    
    # OrderedList, float -> int
    def remove(self, item):
        ''' removes an item from the list, keeps the rest of the list intact, and returns index of 
            the removed item, if not in list return -1 '''
        current = self.head
        index = 0
        # want to go through list
        while current is not None:
            if (current.data == item):
                break
            current = current.next
            index +=1
        # check if reached end without finding
        if current is None:
            return -1
        # assign variables to prev and next nodes
        # must be first spot
        if (index == 0):
            # new front is next item
            self.head = current.next
            # new front's prev is now None
            self.head.prev = None
        # must be last spot
        elif (current.next is None):
            # tail is prev item
            self.tail = current.prev
            # tail next is now None
            self.tail.next = None
        # must be middle
        else:
            # prev's next is current's old next
            current.prev.next = current.next
            # next's prev is current's old prev
            current.next.prev = current.prev
        # decrement and return
        self.num_nodes -= 1
        return index

    # OrderedList, float -> boolean
    def search_forward(self, item):
        ''' returns True if item is in list, False otherwise '''
        current = self.head
        # loop through list to check if item is in there
        while current is not None:
            if current.data == item:
                return True
            # keep going
            current = current.next
        # must not be in the list
        return False
        
    # OrderedList, float -> boolean
    def search_backward(self, item):
        ''' does same as search_forward, but starts at end of list '''
        current = self.tail
        # loop through list to check if item is in there, back to front
        while current is not None:
            if current.data == item:
                return True
            # keep going
            current = current.prev
        # must not be in the list
        return False
        
    # OrderedList -> boolean
    def is_empty(self):
        ''' returns true if OrderedList has no items, false otherwise '''
        return self.num_nodes == 0
    
    # OrderedList -> int
    def size(self):
        ''' returns the number of items in OrderedList '''
        return self.num_nodes
        
    # OrderedList, float -> int
    def index(self, item):
        ''' returns the index of item in OrderedList, if not found return -1 '''
        pass
    
    # OrderedList -> float
    def pop(self, pos = None):
        ''' removes the last node if pos is None, otherwise remove node it in position pos and return its data '''
        pass