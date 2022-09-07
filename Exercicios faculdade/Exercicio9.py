argumentos = ["<", ">", "="]
index = -1

inicio = (int(input("Digite o número inicial: ")))
final = (int(input("Digite o número final: ")))

def inserirNum():
    global index, argumentos
    return argumentos[index]

def randomNum(numInicial, numFinal):
    if numInicial > numFinal:
        return True

    mid = (numInicial + numFinal) // 2

    print("O número é", mid, "?", end = "")
    jogador = input()
    print(jogador)

    if jogador == "=":
        print("Parabens, esse é o numero!")
        return False
    elif jogador == ">" or jogador == "<":
        print("O numero é maior que: ", mid, "?", end = "")
        jogador = input()
        print(jogador)
        if jogador == "=":
            return randomNum(mid + 1, numFinal)
        elif jogador == "<" or jogador == ">":
            return  randomNum(numInicial, mid - 1)
        else:
            print("Entrada Invalida! Digite '<', '>' ou '='  ")
            return randomNum(numInicial, numFinal)
    else:
        print("Entrada Invalida! Digite '<', '>' ou '='")
        return randomNum(numInicial, numFinal)
if __name__ == "__main__":
    numInicial = inicio
    numFinal = final

    output = randomNum(numInicial, numFinal)
    if output:
        print("Escolha melhor!")