class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class DList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def show(self):
		array = []
		if self.head:
			runner = self.head
			while runner:
				array.append(runner.value)
				runner = runner.next
		print array
		return self
	def add_back(self, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			temp = self.tail
			self.tail.next = n
			self.tail = n
			self.tail.prev = temp
		return self
	def delete_node(self, value):
		if not self.head:
			print "nothing to delete"
		else:
			runner = self.head
			while runner:
				if runner.value is value: #only works in the middle so far
					if runner.next and runner.prev:
						runner.prev.next = runner.next
						runner.next.prev = runner.prev
						runner.next = None
						runner.prev = None
						break
					elif not runner.next:
						self.tail = runner.prev
						self.tail.next = None
						break
					elif not runner.prev:
						self.head = runner.next
						self.head.prev = None
						break
				else:
					runner = runner.next
		return self
	def insert_before(self, next_val, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			runner = self.head
			while runner:
				if runner.value is next_val:
					if runner.prev:
						n.next = runner
						n.prev = runner.prev
						runner.prev.next = n
						runner.prev = n
						break
					else:
						n.next = runner
						runner.prev = n
						self.head = n
						break
				else:
					runner = runner.next
		return self
	def insert_after(self, prev_val, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			runner = self.head
			while runner:
				if runner.value is prev_val:
					if runner.next:
						n.next = runner.next
						n.prev = runner
						runner.next.prev = n
						runner.next = n
						break
					else:
						n.prev = runner
						runner.next = n
						self.tail = n
						break
				else:
					runner = runner.next
		return self


d_list = DList()
d_list.add_back("a").add_back("b").add_back("z").delete_node("b").show().insert_before("z", "b").show().insert_after("z", "y").show()
print d_list.tail.prev.value