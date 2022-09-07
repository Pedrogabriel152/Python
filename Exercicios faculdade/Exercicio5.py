valorCompu = float(input("Digite o valor do emprestimo da compra: "))
juros = .01
pagamentoInicial = valorCompu * .1
valorParce = (valorCompu - pagamentoInicial) * .05
mes = 1
saldoDevido = (valorCompu - pagamentoInicial) * 1.01
saldoRestante = saldoDevido - valorParce * 1.01

print("Mes    Saldo Devido   Juros    Valor devido mes    Parcela    Saldo Restante")

while saldoRestante > 0:
	jurosmmes = saldoRestante * juros
	saldoDevido = saldoRestante * 1.01
	valorPrinc = valorParce - jurosmmes
	if saldoRestante > 0:
		saldoRestante -= valorParce * 1.01
	else:
		saldoRestante = 0
		
	print("%2d  %10.2f   %10.2f  %10.2f  %15.2f  %12.2f"%(mes, saldoDevido, jurosmmes, valorPrinc, valorParce, saldoRestante))
	mes += 1

