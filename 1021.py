valorlido = float(input())
valorlido = valorlido+0.001
print ("NOTAS:")
print (int(valorlido//100),"nota(s) de R$ 100.00")
quantidade = (valorlido % 100)
print (int(quantidade//50),"nota(s) de R$ 50.00")
quantidade = (quantidade % 50)
print (int(quantidade//20),"nota(s) de R$ 20.00")
quantidade = (quantidade % 20)
print (int(quantidade//10),"nota(s) de R$ 10.00")
quantidade = (quantidade % 10)
print (int(quantidade//5),"nota(s) de R$ 5.00")
quantidade = (quantidade % 5)
print (int(quantidade//2),"nota(s) de R$ 2.00")
quantidade = (quantidade % 2)
print ("MOEDAS:")
print (int(quantidade//1),"moeda(s) de R$ 1.00")
quantidade = (valorlido % 1)
print (int(quantidade//0.50),"moeda(s) de R$ 0.50")
quantidade = (quantidade % 0.50)
print (int(quantidade//0.25),"moeda(s) de R$ 0.25")
quantidade = (quantidade % 0.25)
print (int(quantidade//0.10),"moeda(s) de R$ 0.10")
quantidade = (quantidade % 0.10)
print (int(quantidade//0.05),"moeda(s) de R$ 0.05")
quantidade = (quantidade%0.05)
print (int(quantidade//0.01),"moeda(s) de R$ 0.01")