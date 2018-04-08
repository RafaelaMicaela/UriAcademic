a,b,c,d = map(int, input().split())
if ((a+b)>c and (a+c)>b and (b+c)>a):
	print("S")
elif ((a+b)>d and (a+d)>b and (b+d)>a):
	print("S")
elif ((d+b)>c and (d+c)>b and (b+c)>d):
	print("S")
elif ((d+a)>c and (d+c)>a and (a+c)>d):
	print("S")
else:
	print("N")	