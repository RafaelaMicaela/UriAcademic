inicio,final = map(int, input().split())
if (inicio > final):
	a=24 - inicio
	h=a + final
	print("O JOGO DUROU %d HORA(S)" %h)
elif(final > inicio):
	h=final - inicio
	print("O JOGO DUROU %d HORA(S)" %h)
elif (inicio==final):
	h=24
	print("O JOGO DUROU %d HORA(S)" %h)