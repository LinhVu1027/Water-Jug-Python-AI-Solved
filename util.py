class Stack:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

	def show(self):
		print self.list

class Queue:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.insert(0, item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

	def show(self):
		print self.list

if __name__ == "__main__":
	stack = Stack()
	stack.isEmpty()
	stack.show()
	stack.push(2)
	stack.push(7)
	stack.push(11)
	stack.show()
	stack.pop()
	stack.show()

	queue = Queue()
	queue.isEmpty()
	queue.show()
	queue.push(2)
	queue.push(7)
	queue.push(11)
	queue.show()
	queue.pop()
	queue.show()