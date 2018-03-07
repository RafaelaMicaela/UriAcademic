notas = [100,50,20,10,5,2]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]
n = float(input())
print ("NOTAS:")
for x in notas:
	if n >= x:
		print("{0} nota(s) de R$ {1}.00".format(n//x,x))
		n %= x
	else:
		print("{0} nota(s) de R$ {1}.00".format(n//x,x))
print ("MOEDAS:")		
for y in moedas:
	if n >= y:
		print("{0} moeda(s) de R$ {1}".format(n//y,y))
		n %= y
	else:
		print("{0} moeda(s) de R$ {1}".format(n//y,y))	