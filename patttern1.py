'''
'''
no  = int(input("enter no"))
for i in range(no+1,0,-1):
	for j in range(0,i-1):
		print("*",end="")

	print()	