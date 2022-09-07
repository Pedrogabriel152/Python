class Student:
	"""docstring for Student"""
	def __init__(self, nome, ponto1 = 0, ponto2 = 0, ponto3 = 0):
		self.nome = nome
		self.ponto1 = ponto1
		self.ponto2 = ponto2
		self.ponto3 = ponto3

	def alteraNome(self,nome):
		self.nome = nome

	def alteraPonto1(self,ponto1):
		self.ponto1 = ponto1

	def alteraPonto2(self,ponto2):
		self.ponto2 = ponto2

	def alteraPonto3(self,ponto3):
		self.ponto3 = ponto3

nome = input("Digite o nome do aluno: ")
ponto1 = int(input("Digite o ponto1: "))
ponto2 = int(input("Digite o ponto2: "))
ponto3 = int(input("Digite o ponto3: "))

aluno = Student(nome,ponto1,ponto2,ponto3)

print("\nNome: ",aluno.nome)
print("Ponto1: ",aluno.ponto1)
print("Ponto2: ",aluno.ponto2)
print("Ponto3: ",aluno.ponto3)

opcao = input("\nDeseja alterar algum dos dados? 'S'-sim e 'N'-nao: ")

if opcao == "S":
	dadoAlterar = int(input("Qual dos dados deseja alterar? 1 - nome, 2- ponto1, 3-ponto3 ou 4-ponto3: "))

	if dadoAlterar == 1:
		nome = input("Digite o nome do aluno: ")
		aluno.alteraNome(nome)

	if dadoAlterar == 2:
		ponto1 = int(input("Digite o ponto1: "))
		aluno.alteraPonto1(ponto1)

	if dadoAlterar == 3:
		ponto2 = int(input("Digite o ponto2: "))
		aluno.alteraPonto2(ponto2)

	if dadoAlterar == 4:
		ponto3 = int(input("Digite o ponto3: "))
		aluno.alteraPonto3S(ponto3)

print("\nNome: ",aluno.nome)
print("Ponto1: ",aluno.ponto1)
print("Ponto2: ",aluno.ponto2)
print("Ponto3: ",aluno.ponto3)