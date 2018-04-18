n = []
for i in range(20):
    i = int(input())
    n.append(i)
y = 0
for j in n[::-1]:
    print ("N[{}] = {}".format(y, j))
    y +=1
