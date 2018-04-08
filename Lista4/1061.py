di = input().split(" ")
w1 = int(di[1])
x1,y1,z1 = map(int, input().split(" : "))
df = input().split(" ")
w2 = int(df[1])
x2,y2,z2 = map(int, input().split(" : "))
dia = (w2 - w1)
hora = (x2 - x1)
minuto = (y2 - y1)
segundo = (z2 -z1)
if (segundo < 0): 
	segundo = 60 + segundo
	minuto = minuto - 1
if (minuto < 0):
	minuto = 60 + minuto
	hora= hora - 1
if (hora < 0):
	hora = 24 + hora
	dia = dia - 1
if (dia <= 0):
	dia = 0

print(dia,"dia(s)")
print(hora,"hora(s)")
print(minuto,"minuto(s)")
print(segundo,"segundo(s)")
