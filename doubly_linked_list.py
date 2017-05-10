# -*- coding: utf-8 -*-

class Node(object):
	"""
	Doubly Linked List Node implementation.
	"""
	def __init__(self, value):
		self.value = value
		self.prevnode = None
		self.nextnode = None
		
# Doubly Linked List implementation example	
if __name__ == "__main__":
	# create three nodes
	a = Node(1)
	b = Node(2)
	c = Node(3)
	# link the nodes together
	a.nextnode = b
	b.prevnode = a
	b.nextnode = c
	c.prevnode = b
	# reference the head and the tail of the list
	head = a
	tail = c
	# print structure created
	print("None <- {} <--> {} <--> {} -> None".format(head.value, head.nextnode.value, tail.value))