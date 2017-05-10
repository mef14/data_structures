# -*- coding: utf-8 -*-

class BinaryTree(object):
	"""
	Binary Tree implementation.
	"""
	def __init__(self, key):
		self.key = key
		self.leftChild = None
		self.rightChild = None
		
	def insertLeft(self, newNode):
		
		t = BinaryTree(newNode)
		
		if not self.leftChild:
			self.leftChild = t
		else:
			t.leftChild = self.leftChild
			self.leftChild = t
			
	def insertRight(self, newNode):
	
		t = BinaryTree(newNode)
	
		if not self.rightChild:
			self.rightChild = t
		else:
			t.rightChild = self.rightChild
			self.rightChild = t
			
	def getRootKey(self):
		return self.key
		
	def setRootKey(self, newkey):
		self.key = newkey
		
	def getLeftChild(self):
		return self.leftChild
		
	def getRightChild(self):
		return self.rightChild
		
if __name__ == "__main__":
	# create a binary tree
	root = BinaryTree(1)
	root.insertRight(3)
	root.getRightChild().insertRight(6)
	root.insertLeft(2)
	root.getLeftChild().insertLeft(4)
	root.getLeftChild().insertRight(5)
	# print the tree
	print("Binary tree representation:\n")
	print("      {}      ".format(root.getRootKey()))
	print("     / \      ")
	print("   {}    {}   ".format(root.getLeftChild().getRootKey(), root.getRightChild().getRootKey()))
	print("  / \    \    ")
	print("{}    {}    {}".format(root.getLeftChild().getLeftChild().getRootKey(), root.getLeftChild().getRightChild().getRootKey(), root.getRightChild().getRightChild().getRootKey()))