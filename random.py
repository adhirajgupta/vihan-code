no1 = int(input("pls enter value of no1 ="))
no2 = int(input("pls enter value of no2 ="))
no3 = int(input("pls enter value of no3 ="))
no4 = int(input("pls enter value of no4 ="))

if no1>no2 and no3 and no4:
	print("no1 is greatest")
if no2>no1 and no3 and no4:
	print("no2 is greatest")
if no3>no2 and no1 and no4:
	print("no3 is greatest")
else:
	print("no4 is greatest")