n = float(input("Digite o valor de n: "))

# Exercicio 1 a)
if 2**n > -4*(n**2) and 2**n > 5*n:
	print("O termo predominante do exercicio 1 a) e 2 elevado a n")
elif -4*(n**2) > 2**n and -4*(n**2) > 5*n:
	print("O termo predominante do exercicio 1 a) e -4n elevado a 2")
elif 5*n > 2**n and -4*(n**2) < 5*n:
	print("O termo predominante do exercicio 1 a) e 5n")
else:
	print("Para esse n os algoritmo realizam o mesmo trabalho")

# Exercicio 1 b)
if 3*(n**2) > 6:
	print("O termo predominante do exercicio 1 b) e 3n elevado a 2")
elif 3*(n**2) < 6:
	print("O termo predominante do exercicio 1 b) e 6")
else:
	print("Para esse n os algoritmo realizam o mesmo trabalho")

# Exercicio 1 c)
if n **3 > n**2 and n**3 > -n:
	print("O termo predominante do exercicio 1 c) e n elevado a 3")
elif n**2 > n**3 and n**2 > -n:
	print("O termo predominante do exercicio 1 c) e n elevado a 2")
elif -n > n**2 and n**3 < -n:
	print("O termo predominante do exercicio 1 c) e -n")
else:
	print("Para esse n os algoritmo realizam o mesmo trabalho")