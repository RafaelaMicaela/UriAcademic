a,b = input().split()
codigo = int(a)
quantidade = int(b)
if codigo == 1:
    total= ( quantidade*4)
    total_srt = "{:.2f}".format(total)
    print("Total: R$",total_srt)
if codigo == 2:
    total= (quantidade*4.50)
    total_srt = "{:.2f}".format(total)
    print("Total: R$",total_srt)
if codigo== 3:
    total = (quantidade*5)
    total_srt = "{:.2f}".format(total)
    print("Total: R$",total_srt)
if codigo == 4:
    total= (quantidade*2)
    total_srt = "{:.2f}".format(total)
    print ("Total: R$",total_srt)
if codigo== 5:
    total= quantidade*1.5
    total_srt = "{:.2f}".format(total)
    print ("Total: R$",total_srt)
