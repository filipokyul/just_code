y = int(input("Insert a number: "))

for x in range(1,y,2):
	print(" "*int((y-x)/2), "*"*x, " "*int((y-x)/2))
