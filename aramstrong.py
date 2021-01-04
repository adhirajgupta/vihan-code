no = int(input("enter no"))
cnt=0
tempno = no
add =0
a =1
while(no>0):
	a = no % 10 
	cnt= cnt+1 
	add = add + (a**cnt)  
	no = no//10



if tempno == add:
	print("armstrong no")
else:
	print("not armstrong no")	

