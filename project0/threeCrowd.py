names = ['bob', 'suzy', 'bertha', 'bartholomew']

def crowd_test(names):
	if (len(names) > 3):
		print("The room is crowded")

crowd_test(names)

del names[0]
del names[1]

crowd_test(names)