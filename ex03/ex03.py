def busca_linear(arr: list, alvo: int) -> int:
    """
    Realiza busca linear e exibe cada passo.
    Retorna o índice do elemento encontrado, ou -1 se não encontrado.
    """
    passos = 0

    for i, valor in enumerate(arr):
        passos += 1
        print(f"  Passo {passos}: índice {i} → valor {valor}", end="")

        if valor == alvo:
            print(f" ENCONTRADO!")
            print(f"\nTotal de passos: {passos}")
            return i

        print()  # Nova linha se não encontrou

    print(f"\nValor {alvo} NÃO encontrado. Total de passos: {passos}")
    return -1

if __name__ == "__main__":
    array = [2, 4, 6, 8, 10, 12, 13]
    alvo = 8

    print(f"Array : {array}")
    print(f"Buscando: {alvo}\n")
    resultado = busca_linear(array, alvo)
    print(f"\nÍndice do elemento: {resultado}")
