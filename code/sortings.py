# inseration sort

class InserationSort():
	def sorting(self, unsorted):
		for item in unsorted:
			idx = unsorted.index(item)
			while idx > 0:
				if unsorted[idx-1] > unsorted[idx]:
					unsorted[idx], unsorted[idx-1] = unsorted[idx-1], unsorted[idx]
				else:
					break;
				idx = idx-1


#insert_sort = InserationSort()
#list1 =[2,4,1,88,23,22]
#insert_sort.sorting(list1)
#print list1


	
