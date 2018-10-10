def maior2(a, b):
    if(a > b):
        maior = a
    if(b > a):
        maior = b 
    return maior

x = int(input())
y = int(input())
print(maior2(x,y))


def maior5 (a, b, c, d, e):
    return 0

def quantidade_de_vogais(s):
    return 0

def impar(n):
    return False

def conta_palavras(texto):
    return 0

def intervaloab(n1, n2):
    return []

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
