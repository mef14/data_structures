# -*- coding: utf-8 -*-

class Deque(object):
    """
    Implementation of a deque.
    """
    def __init__(self):
        """
        Create an empty deque.
        """
        self.items = []
        
    def isEmpty(self):
        """
        Check if the deque is empty.
        """
        return not self.items
    
    def addFront(self, new_item):
        """
        Push a new item to the front of the deque.
        """
        self.items.append(new_item)
        
    def addRear(self, new_item):
        """
        Push a new item to the rear of the deque.
        """
        self.items = [new_item] + self.items
        
    def removeFront(self):
        """
        Pop the item on the front out.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            return
    
    def removeRear(self):
        """
        Pop the item on the rear of the deque.
        """
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return
        
    def size(self):
        """
        Return the size of the deque.
        """
        return len(self.items)
    
    def deque(self):
        """
        Return the deque.
        """
        return self.items
    
    def rear(self):
        """
        Return the rear of the deque without removing it.
        """
        if not self.isEmpty():
            return self.items[0]
        else:
            return
        
    def front(self):
        """
        Return the front of the deque without removing it.
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            return