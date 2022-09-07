import time

problemSize = 10000000
print("%12s%16s"%("ProblemSize", "Seconds"))
while problemSize>0:
	problemSize = problemSize // 2
	start = time.time()
	#O inicio do algoritmo
	work = 1
	while problemSize>0:
		problemSize = problemSize // 2
		work +=1
		work -=1
	#fim do algoritmo
	elapsed = time.time() - start
	print("%12d%16.3f"%(problemSize, elapsed))
	problemSize *= 2