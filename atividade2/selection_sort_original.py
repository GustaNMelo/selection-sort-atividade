import time

def selection_sort_basico(lista):
    iteracoes = 0
    for i in range(len(lista) - 1):
        pos_menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        if pos_menor != i:
            lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
            print(f'Troca: {lista[i]} <-> {lista[pos_menor]}')
        iteracoes += 1
        print(f'Iteração {iteracoes}: {lista}')
    return iteracoes
