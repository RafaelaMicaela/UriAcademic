a,b,c = map(int, input().split())
if (a<b+c) and (b<c+a) and (c<b+a):
	if (a*a < b*b + c*c):
		print("a")
	elif(a*a > b*b + c*c):
		print("o")
	if(a*a == b*b + c*c):
		print("r")
else:
	print("n")