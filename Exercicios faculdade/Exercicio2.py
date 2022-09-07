salarioHora = float(input("Entre com valor do salario hora: "))
totalHoras = float(input("Entre com o total de horas regulares que o funcionario teve: "))
horasExtras = float(input("Entre com o total de horas extres: "))

salarioSemanalRegular = salarioHora * totalHoras
totalExtras = horasExtras * (1.5 * salarioHora)
salarioTotal = salarioSemanalRegular + totalExtras

print("O salario semanal foi de: ",salarioTotal," reais")