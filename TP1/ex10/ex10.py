def bubbleSort(lista):
    for last in range(len(lista) - 1, 0, -1):
        for inner in range(last):
            if lista[inner] > lista[inner + 1]:
                lista[inner], lista[inner + 1] = lista[inner + 1], lista[inner]
    return lista


# Testes
print(bubbleSort(["banana", "abacaxi", "laranja", "uva", "kiwi"]))
print(bubbleSort(["zebra", "abelha", "macaco", "girafa"]))
print(bubbleSort(["python", "java", "rust", "go"]))