alturaInicial = float(input("Entre com a altura inicial da bola: "))
vezesQuicando = int(input("Digite quantas vezes a bola vai quicar: "))
alturaVariada = alturaInicial
alturaTotal = 0
inicio = 1

while inicio <= vezesQuicando:
	alturaQuique = alturaVariada * 0.6

	if inicio < vezesQuicando:
		alturaTotal += (alturaQuique * 2)

	if inicio == vezesQuicando:
		alturaTotal += alturaQuique
			
	alturaVariada = alturaQuique
	inicio += 1

alturaTotal += alturaInicial 

print("A altura a distancia total foi de: %0.2f" % alturaTotal)