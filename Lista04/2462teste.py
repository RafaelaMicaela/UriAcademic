a,b,c,d = input().split()
h1,m1 = a.split(":")
h2,m2 = b.split(":")
h3,m3 = c.split(":")
h4,m4 = d.split(":")
minutos1 = (h1*60)+m1
minutos2 = (h2*60)+m2
diferenca1 = (minutos2 - minutos1)
minutos3 = (h3*60)+m3
minutos4 = (h4*60)+m4
diferenca2 = (minutos4 - minutos3)
duracao = (diferenca1 + diferenca2)/2
variacao = (diferenca1 - duracao)/60
if (duracao < 0):
	diferenca1 += 24 * 60

duracao = (diferenca1 + diferenca2)/2
variacao= (diferenca1 - duracao)/60

if (variacao > 12):
	variacao = (variacao - 12 )+(-12)
elif (variacao < -12):
	variacao = ((variacao *(-1)) - 12 + (-12))
print (int(duracao), int(variacao)) 
