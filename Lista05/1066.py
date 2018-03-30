total = 5
pares = 0
positivos = 0
negativos = 0
for i in range(total):
    num = int(input())
    if (num % 2 == 0):
        pares += 1
    if (num > 0):
        positivos += 1
    elif (num < 0):
        negativos += 1

print((pares),"valor(es) par(es)")
print(total - pares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")

