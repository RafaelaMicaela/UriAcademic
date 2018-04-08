num = int(input())
c = 0
for x in range(2,int(num//2+1)):
  if (num%x==0):
    c+=1
    print('S')
    break
if(c==0):
  print('N')
		
		




