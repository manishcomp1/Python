class Searching():
	def binary(self, list1, sidx, eidx, element):
	    if eidx >= sidx:
		midx= sidx + (eidx - sidx)/2
		if element == list1[midx]:
		    print"Found", midx
		    return midx
		elif element > list1[midx]:
			self.binary(list1, midx+1,eidx ,element)
		elif element < list1[midx]:
			self.binary(list1, sidx, midx -1, element)
		else:
			return -1

sObj = Searching()
list1 = [1,3,5,33,55,22,444,232,43]
list1.sort()
sObj.binary(list1, 0, len(list1)-1, 22)
		
