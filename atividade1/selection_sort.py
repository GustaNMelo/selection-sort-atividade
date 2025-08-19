def selection_sort(lista):
    pos = 0
    while pos < len(lista) - 1:
        menor_primeiro(lista, pos)
        pos += 1
        print(f'Iteração {pos}: {lista}')

def menor_primeiro(lista, pos):
    menor = lista[pos]
    posMenor = pos
    for i in range(pos + 1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posMenor = i
    if posMenor != pos:
        lista[pos], lista[posMenor] = lista[posMenor], lista[pos]
        print(f'Troca: {lista[pos]} <-> {lista[posMenor]}')

# Testando o código com entrada de usuário
entrada = input("Digite uma lista de números separados por espaço: ")
lista = list(map(int, entrada.split()))
print("Lista original: ", lista)
selection_sort(lista)
print("Lista ordenada: ", lista)
