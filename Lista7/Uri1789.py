lesmas = int(input())
velocidade = []
while (lesmas):
    velocidade = list(map(int, input().split()))
    maior = velocidade[0]
    for i in range(lesmas):
        if maior < velocidade[i]:
            maior = velocidade[i]
    if maior < 10:
        print("1")
    if maior >= 10 and maior < 20:
        print("2")
    if maior >= 20:
        print("3")
     
