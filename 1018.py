notas = [100,50,20,10,5,2,1]
n = int(input())
print(n)
for x in notas:
	if n >= x:
		print("{0} nota(s) de R$ {1},00".format(n//x,x))
		n %= x
	else:
		print("{0} nota(s) de R$ {1},00".format(n//x,x))