alcool,gasolina,renda,rendg = map(float, input().split())
if ((alcool / renda)<(gasolina/rendg)):
	print("A")
else:
	print("G")