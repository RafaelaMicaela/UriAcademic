a1 = int(input())
a2 = int(input())
a3 = int(input())
ai1= (2* a2 + 4 *a3)
ai2= (2* a1 + 2 * a3)
ai3= (4* a1 + 2 * a2)
if (ai1 <= ai2) and (ai1 <= ai3):
	print(ai1)
elif(ai2 <= ai3):
	print(ai2)
else:
	print(ai3)

