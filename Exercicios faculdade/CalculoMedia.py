nota = float(input("Entre com a nota 1: "))
nota2 = float(input("Entre com a nota 2: "))
nota3 = float(input("Entre com a nota 3: "))

media = (nota + nota2 + nota3)/3
print("A media foi de: ",media)

if media < 6:
	print("O aluno foi reprovado")
else:
	print("O aluno foi aprovado")