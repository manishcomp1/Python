class Base:

	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def name(self):
		return self.fname + " " + self.lname

class Derived(Base):

	def __init__(self, fname, lname, staff_name):
		#super().__init__(fname, lname)
		Base.__init__(self, fname, lname)
		self.staff_name = staff_name

obj = Base('Manish', 'Kumar')	
obj2 = Derived('Manish', 'kumar', 'singh')
name = obj.name()
print name

