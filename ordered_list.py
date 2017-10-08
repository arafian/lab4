#Arman Rafian
#Section 7

class Node:
    ''' impliments a node item that will be the unit for OrderedList '''
    def __init__(self, data):
        self.data = data # data is a float representing a numeric value that the node holds
        self.next = None # next is an adress pointing to the next node in OrderedList
        
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
        pass
    
    # OrderedList, float -> int
    def remove(self, item):
        ''' removes an item from the list, keeps the rest of the list intact, and returns index of 
            the removed item, if not in list return -1 '''
        pass
            
    # OrderedList, float -> boolean
    def search_forward(self, item):
        ''' returns True if item is in list, False otherwise '''
        pass
        
    # OrderedList, float -> boolean
    def search_backward(self, item):
        ''' does same as search_forward, but starts at end of list '''
        pass
        
    # OrderedList -> boolean
    def is_empty(self):
        ''' returns true if OrderedList has no items, false otherwise '''
        pass
    
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

        
    