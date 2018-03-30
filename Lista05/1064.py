qtd = 0
media = 0
for x in range(0,6):
	num = float(input())
	if (num> 0):
		qtd = qtd +1
		media += num
print(qtd,"valores positivos")
mediaf = media/qtd
print("{:.1f}".format(mediaf))

	