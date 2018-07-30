class Calculations():

	def inst_method(self):
		print "Hello !!, I am inside inst_method"

	@staticmethod
	def add(x , y):
		return x +y

	@classmethod
	def multiplication(cls, x , y):
		return x*y

print Calculations.multiplication(5, 4)
obj = Calculations()
print obj.add(5, 4)
print obj.inst_method()
