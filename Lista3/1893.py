ontem,hoje = map(int, input().split())
if (3 <= hoje and hoje <= 96 and hoje>ontem):
    print("crescente")
elif(3<=hoje and hoje <= 96 and hoje<ontem):
    print("minguante")
elif(0<=hoje and hoje<=2):
    print("nova")
elif(97 <= hoje and hoje <=100):
    print("cheia")
