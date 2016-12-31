class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class SList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def show(self):
		array = []
		if self.head:
			runner = self.head
			while(runner):
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
			self.tail.next = n
			self.tail = n
		return self
	def add_front(self, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			temp = self.head
			self.head = n
			self.head.next = temp
		return self
	def insert_before(self, next_val, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			runner = self.head
			while(runner.next):
				if runner.next.value is next_val:
					temp = runner.next
					runner.next = n
					n.next = temp
					break
				else:
					runner = runner.next
		return self
	def insert_after(self, preval, value):
		n = Node(value)
		if not self.head:
			self.head = n
			self.tail = n
		else:
			runner = self.head
			while(runner):
				if runner.value is preval:
					temp = runner.next
					runner.next = n
					n.next = temp
					break
				else:
					runner = runner.next
		return self
	def remove_node(self, value):
		if not self.head:
			print "list already empty"
		elif not self.head.next:
			if self.head.value is value:
				self.head = None
		else:
			runner = self.head
			while(runner.next):
				if runner.next.value is value:
					temp = runner.next
					runner.next = runner.next.next
					temp.next = None
				else:
					runner = runner.next
		return self
	def reverse_list(self):
		array = []
		if not self.head:
			pass
		else:
			while(self.head):
				array.insert(0, self.head.value)
				self.head = self.head.next
			for item in array:
				self.add_back(item)
		return self


s_list = SList()
s_list.add_back("z").add_front("a").insert_before("z", "y").insert_after("a", "b").remove_node("z").reverse_list().show()