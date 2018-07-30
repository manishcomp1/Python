def prime_num():
	composit = []
	for data in range(3, 50):
		for item in range(2,8):
			if item != data:
				if data%item == 0:
					composit.append(data)

	
	print"composit---",set(composit)
	print"prime number",set(range(3,50)) - set(composit) 
		
		
result = prime_num()	
	
	
