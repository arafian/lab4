#Arman Rafian
#Section 7

class Node:
    ''' impliments a node item that will be the unit for OrderedList '''
    def __init__(self, data):
        self.data = data # data is a float representing a numeric value that the node holds
        self.next = None # next is an adress pointing to the next node in OrderedList
        self.prev = None
        
    def __repr__(self):
        return (self.data, self.next)
        
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
        
    # OrderedList, float ->
    def add(self, item):
        ''' adds an item to the list in its correct spot, assume that the item is not already in list '''
        current = self.head
        prev = None
        while (current is not None):
            prev = current
            current = current.next
            if (current.data > item):
                break
        # must be first element
        if (prev is None):
            new_node = Node(item)
            # assign forwad connection
            new_node.next = current
            # assign next's backwards connection
            current.prev = new_node
            # by definition backwards must be None
            new_node.prev = None
            # new node is now first node in list
            head = new_node
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
        self.num_nodes += 2 #*** 1
    
    # OrderedList, float -> int
    def remove(self, item):
        ''' removes an item from the list, keeps the rest of the list intact, and returns index of 
            the removed item, if not in list return -1 '''
        current = self.head
        index = 1 #******* 0
        # want to go through list
        while current is not None:
            if (current.data == self):
                break
            current = current.next
            index +=1
        # check if reached end without finding
        if current is None:
            return -1
        # assign variables to prev and next nodes
        prev_node = current.prev
        next_node = current.next
        # update connections of nodes
        prev_node.next = current.next
        next_node.prev = current.prev
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
        pass
        
    # OrderedList, float -> int
    def index(self, item):
        ''' returns the index of item in OrderedList, if not found return -1 '''
        pass
    
    # OrderedList -> float
    def pop(self, pos = None):
        ''' removes the last node if pos is None, otherwise remove node it in position pos and return its data '''
        pass