pi = 3.1415
interacao = int(input("Digite o numero de interacoes que deseja realizar: "))
resultado = 1 -(1/3)
y = 2
x = 1;

while x <= interacao:
 	
	if x%2 == 0:
 		resultado += +(1/(3 + y))

	if x%2 == 0:
 		resultado += -(1/(3 + y))

	y += 2
	x += 1

resultado1 = resultado * 4

print(resultado1)