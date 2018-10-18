def maior_elemento(l):
    maior = 0
    for i in len(l):
        if (l[i] > maior):
            maior = l[i]
    return maior

def quantidade_de_elementos(maior,l):
    quantidade = 0
    for i in l:
        if (l[i] == maior):
            quantidade = quantidade + 1
    return quantidade

def remover(l,maior):
    for i in l:
        if (maior == l[i]):
            del l[i]
            i = i - 1
    return l

n = int(input())
k = int(input())
l = [n]
for i in range(n):
    l.append(int(input()))
maior = maior_elemento(l) 
quantidade = quantidade_de_elementos(maior,l)
l = remover(l,maior)
if (k <= quantidade):
    print(quantidade)
else:
    maior = maior_elemento(l)
    quantidade = quantidade_de_elementos(maior,l)
    print(quantidade)
