no = int(input("enter no to find length"))
cnt =0
while(no>0):
	a = no % 10
	cnt= cnt+1
	no = no // 10  

print("len of no = ",cnt)	

