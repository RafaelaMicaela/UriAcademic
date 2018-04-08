tempogasto = int (input())
velocidademedia = int (input())
litros = (tempogasto * velocidademedia)/12
litros_srt = "{:.3f}".format(litros)
print (litros_srt)