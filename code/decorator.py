def sample_decorator(addition):
	def wrapper(x, y):
		print x,y
		return addition(x, y)
	return wrapper

@sample_decorator
def addition1(x, y):
	result = x + y
	print "result",result	
	return result

x = 5
y = 10
result = addition1(x , y)
print result
	
