# -*- coding: utf-8 -*-

class Node(object):
	"""
	Singly Linked List Node implementation.
	"""
	def __init__(self, value):
		self.value = value
		self.nextnode = None
	
# Singly Linked List implementation example	
if __name__ == "__main__":
	# create three nodes
	a = Node(1)
	b = Node(2)
	c = Node(3)
	# link the nodes together
	a.nextnode = b
	b.nextnode = c
	# reference head and tail
	head = a
	tail = c
	# print structure
	print("Structure created:\n")
	print("{} -> {} -> {} -> None".format(head.value, head.nextnode.value, tail.value))