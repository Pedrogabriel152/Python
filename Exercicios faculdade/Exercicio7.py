import statistics

list = [1, 4, 4, 6, 8, 9, 10, 5]

def mediana(lista):
    numMeio = len(lista) // 2
    lista.sort()
    if not len(lista) % 2:
        return (lista[numMeio - 1] + lista[numMeio]) / 2.0
    return lista[numMeio]

print("A mediana  é :", mediana(list))

print("O numero que aparece com maior frequência: ", statistics.mode(list))