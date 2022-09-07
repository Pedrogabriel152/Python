import linecache

arquivo = open("funcionario.txt", "r")

nomeArquivo = input("Insira o nome do arquivo: ")

if nomeArquivo == "funcionario":
    print("Arquivo encontrado com sucesso!")
    numLinha = int(input("Insira o numero da linha do arquivo: "))
    if numLinha == 0:
        print("Numero de linha nao existe.")
    else:
        mostrarLinha = linecache.getline("funcionario.txt", numLinha)
        print(mostrarLinha)
        if mostrarLinha == "":
            print("Essa linha não possui conteúdo.")
else:
    print("Arquivo inexistene")