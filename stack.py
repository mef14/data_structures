# -*- coding: utf-8 -*-

class Stack(object):
    """
    Implementation of a stack.
    """
    def __init__(self):
        """
        Create an empty stack.
        """
        self.items = []
        
    def push(self, new_item):
        """
        Push an item to the stack.
        """
        self.items.append(new_item)
        
    def pop(self):
        """
        Pop an item out of the stack.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            return
        
    def size(self):
        """
        Return the size of the stack.
        """
        return len(self.items)
    
    def isEmpty(self):
        """
        Check if the stack is empty.
        """
        return not self.items
    
    def peek(self):
        """
        Return the last item of the stack without removing it.
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            return
    
    def stack(self):
        """
        Return the stack.
        """
        return self.items