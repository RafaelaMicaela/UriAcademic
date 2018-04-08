c1,p1,c2,p2 = map(int, input().split())
if (c1*p1==c2*p2):
	print("0")
elif (c1*p1>c2*p2):
	print("-1")
else:
	print("1")
