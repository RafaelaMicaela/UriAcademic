a,b,c = [int(i) for i in input().split()]
if a < b:
    a,b = b,a
if a < c:
    a,c = c, a
if (a>= b + c):
	print("n")
elif(a*a < b*b + c*c):
	print("a")
elif(a*a > b*b + c*c):
	print("o")
elif(a*a == b*b + c*c):
	print("r")
