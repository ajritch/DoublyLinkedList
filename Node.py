class Node(object):

	def __init__(self, value, prev = None, next = None):
		self.value = value
		self.prev = prev
		self.next = next

	#method to display the node
	def printNode(self):
		print "Value:", self.value, "|", "Next:", self.next, "|", "Prev:", self.prev	