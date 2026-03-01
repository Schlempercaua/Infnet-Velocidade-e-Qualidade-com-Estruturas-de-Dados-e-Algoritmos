def bubbleSort(lista):
    for last in range(len(lista) - 1, 0, -1):
        for inner in range(last):
            if lista[inner] > lista[inner + 1]:
                lista[inner], lista[inner + 1] = lista[inner + 1], lista[inner]
    return lista


# Testes
print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))
print(bubbleSort([5, 4, 3, 2, 1]))
print(bubbleSort([1, 2, 3, 4, 5]))
print(bubbleSort([3, 3, 1, 2, 3]))