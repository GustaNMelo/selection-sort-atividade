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
