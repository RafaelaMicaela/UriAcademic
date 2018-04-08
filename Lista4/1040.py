n1,n2,n3,n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4)/10
media_str ="{:.1f}".format(media)
print("Media:",media_str)
if (media>=7.0):
	print("Aluno aprovado.")
elif (5 <= media < 7):
	print("Aluno em exame.")
	ne = float(input())
	ne_str= "{:.1f}".format(ne)
	print("Nota do exame:",ne_str)
	if (ne + media)/2>=5:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final:",format((ne+media)/2,".1f"))
else:
	print("Aluno reprovado.")	