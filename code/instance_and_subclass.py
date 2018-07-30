class Parent:
	def __init__(self, fname):
		self.fname = fname

	def name(self):
		return self.fname

class Child(Parent):
	def __init__(self, lname):
		self.lname = lname

	def name2(self):
		self.lname = lname


x = Parent('Manish')
y = Child('Kumar')

print isinstance(x, Parent)
print issubclass(Child, Parent)
print issubclass(Parent, Child)
