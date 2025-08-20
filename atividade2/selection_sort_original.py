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

def selection_sort_otimizado(lista):
    iteracoes = 0
    for i in range(len(lista) - 1):
        pos_menor = i
        houve_troca = False
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        if pos_menor != i:
            lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
            houve_troca = True
            print(f'Troca: {lista[i]} <-> {lista[pos_menor]}')
        iteracoes += 1
        print(f'Iteração {iteracoes}: {lista}')
        if not houve_troca:
            print("Nenhuma troca realizada — lista já ordenada. Encerrando.")
            break
    return iteracoes

import time

def testar_versoes(lista):
    print("\n🔵 Versão básica:")
    lista1 = lista.copy()
    inicio = time.time()
    iter_b = selection_sort_basico(lista1)
    tempo_b = time.time() - inicio
    print(f"Total de iterações: {iter_b}")
    print(f"Tempo de execução: {tempo_b:.6f} segundos")

    print("\n🟢 Versão otimizada:")
    lista2 = lista.copy()
    inicio = time.time()
    iter_o = selection_sort_otimizado(lista2)
    tempo_o = time.time() - inicio
    print(f"Total de iterações: {iter_o}")
    print(f"Tempo de execução: {tempo_o:.6f} segundos")
