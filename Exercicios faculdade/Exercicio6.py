#Cria o objeto de leitura do arquivo
arquivo = open("funcionario.txt", "r")

nomeArquivo = input(("Digite o nome do arquivo do usuario: "))

if nomeArquivo == "funcionario":
    print(arquivo.read())