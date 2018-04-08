n = int (input())
horas = int(n / 3600) 
n = n % 3600
m = int(n /60)
s = n % 60
print (str(horas)+":"+str(m)+":"+str(s))