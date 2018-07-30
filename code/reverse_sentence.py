def reverse_sentence():

	input_str = "my name is manish"
	output_str1(input_str)
	output_str2(input_str)
	output_str3(input_str)

	# Expected output
	#output_str1 = "manish is name my"
	#output_str2 = "ym eman si hisnam"
	#output_str3 = "hisnam si eman ym"

def output_str1(input_str):
	os1 = input_str.split(" ")
	os_rev = os1[::-1]
	os_rev2 = " ".join(os_rev)
	print os_rev2

def output_str2(input_str):
	os1 = input_str.split(" ")
	os_rev = [word[::-1] for word in os1]
	os_rev2 = " ".join(os_rev)
	print os_rev2

def output_str3(input_str):
	os1 = input_str.split(" ")
	os_rev = [word[::-1] for word in os1[::-1]]
	os_rev2 = " ".join(os_rev)
	print os_rev2

reverse_sentence()
