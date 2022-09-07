n = float(input("Digite o valor de n: "))

if n**2 > ((1/2)*(n**2)+(1/2)*n):
	print("Para esse n o algoritmo A realiza mais trabalho")
elif n**2 < ((1/2)*(n**2)+(1/2)*n):
	print("Para esse n o algoritmo B realiza mais trabalho")
else:
	print("Para esse n os algoritmo realizam o mesmo trabalho")



if n**4 > 2*n:
	print("Para esse n o algoritmo n elevado a 4 e melhor que 2 elevado a n")
elif n**4 < 2*n:
	print("Para esse n o algoritmo n elevado a 4 e pior que 2 elevado a n")
else:
	print("Os dois sao iguais para esse n")