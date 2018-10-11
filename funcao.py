def maior2(a, b):
    if(a > b):
        maior = a
    if(b > a):
        maior = b 
    return maior

x = int(input())
y = int(input())
print("Questão 1", maior2(x,y))

def maior5(a,b,c,d,f):
    lista = [a,b,c,d,f]
    maior = lista[0]
    for i in range(1,5):
        if (maior < lista[i]):
            maior = lista[i]
    return maior

a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())
print("Questao 2",maior5(a,b,c,d,f))

def quantidade_de_vogais(s):
    quantidadeDeVogais = 0
    for i in range(len(s)):
        if (s[i] == "a" or s[i] == "A"):
            quantidadeDeVogais = quantidadeDeVogais + 1
        elif(s[i] == "e" or s[i] == "E"):
            quantidadeDeVogais = quantidadeDeVogais + 1
        elif(s[i] == "i" or s[i] == "I"):
            quantidadeDeVogais = quantidadeDeVogais + 1
        elif(s[i] == "o" or s[i] == "O"):
            quantidadeDeVogais = quantidadeDeVogais + 1
        elif(s[i] == "u" or s[i] == "U"):
            quantidadeDeVogais = quantidadeDeVogais + 1
    return quantidadeDeVogais

oracao = input()
print("Questao 3:", quantidade_de_vogais(oracao))


def impar(n):
    resultado = False
    if (n % 2 != 0):
        resultado = True
    return resultado

numero = int(input())
print("Questao 4:", impar(numero))

def conta_palavras(texto):
   palavras = [] 
   palavras = texto.split()
   return len(palavras)

texto = input()
print("Questao 5:", conta_palavras(texto))

def intervaloab(n1, n2):
    lista = []
    if (n1 >= n2):
        for i in range(n2,n1+1):
            lista.append(i)
    elif (n2 > n1):
        for i in range(n1, n2+1):
            lista.append(i)
    return lista

a = int(input())
b = int(input())
print("Questao 6:", intervaloab(a,b))

def fatorial(n):
    return 0

def divisores(n):
    return []

def primo(n):
    return False

def primos_entre_si(n1, n2):
    return False

def mdc(n1, n2):
    return 0

def mmc (n1, n2):
    return 0

def transcreve_numero(telefone):
    return ""

def coincidencia_lista(lista1, lista2):
    return []




# Testes
print("Questao 1", maior2(2, 3)==5)
print("Questao 2", maior5(6,8,-1,2,4)==8)
print("Questao 3", quantidade_de_vogais("Abc e america")==6)
print("Questao 4", impar(7))
print("Questao 5", conta_palavras("Isto é um texto")== 4)
print("Questao 6", intervaloab(2,7)==[2,3,4,5,6,7])
print("Questao 7", fatorial(4) == 24)
print("Questao 8", divisores(8) == [1,2,4,8])
print("Questao 9", primo(11))
print("Questao 10",primos_entre_si(8, 15))
print("Questao 11",mdc(6, 10)==2)
print("Questao 12",mmc(6, 10)==30)
print("Questao 13",transcreve_numero("12")==["um", "dois"])
print("Questao 14",coincidencia_lista([1,2,3,4], [0,2,6,8])==1)
