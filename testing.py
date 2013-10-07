list1 = ['a','b','c','d']
list2 = ['b','a','d','c']

hits = []
for word in list1:
    if word in list2 and word not in hits:
		hits.append(word)
		if len(hits) == len(list2):
			print list2
