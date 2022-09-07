import time
count = 0
problemSize = int(input("Digite o tamanho do problema: "))
while problemSize>0:
	problemSize = problemSize // 2
	count += 1

print(count)