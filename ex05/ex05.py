def greatestNumber_on(array):
    maior = array[0]          # Assume o primeiro como maior

    for numero in array:      # Percorre o array uma única vez → O(N)
        if numero > maior:
            maior = numero

    return maior

# Testes
arrays = [
    [3, 7, 1, 9, 4, 2],
    [10, 5, 8, 3],
    [1],
    [-5, -1, -3],
]

for arr in arrays:
    print(f"Array: {arr}")
    print(f" O(N) : {greatestNumber_on(arr)}")
    print()
