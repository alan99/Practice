list1 = [1,2,2,4,5]
n = len(list1)

for i in range(n):
	try:
		k = list1.index(i)
		print(i, "at", k)
	except:
		print("Not found")

