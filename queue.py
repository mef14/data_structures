# -*- coding: utf-8 -*-

class Queue(object):
    """
    Implementation of a queue.
    """
    def __init__(self):
        """
        Create an empty queue.
        """
        self.items = []
        
    def enqueue(self, new_item):
        """
        Enqueue a new item.
        """
        self.items = [new_item] + self.items
        
    def dequeue(self):
        """
        Dequeue the item on the front of the queue.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            return
    
    def size(self):
        """
        Return the size of the queue.
        """
        return len(self.items)
    
    def isEmpty(self):
        """
        Check if the queue is empty.
        """
        return not self.items
    
    def rear(self):
        """
        Return the rear of the queue.
        """
        if not self.isEmpty():
            return self.items[0]
        else:
            return
    
    def front(self):
        """
        Return the front of the queue without removing it.
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            return
    
    def queue(self):
        """
        Return the queue.
        """
        return self.items