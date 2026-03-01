def busca_binaria(arr: list, alvo: int) -> int:
    """
    Realiza busca binária e exibe cada passo.
    Retorna o índice do elemento encontrado, ou -1 se não encontrado.
    """
    esquerda = 0
    direita = len(arr) - 1
    passos = 0

    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        valor_meio = arr[meio]

        print(f"  Passo {passos}: esquerda={esquerda}, direita={direita}, "
              f"meio={meio}, arr[meio]={valor_meio}", end="")

        if valor_meio == alvo:
            print(f" ENCONTRADO!")
            print(f"\nTotal de passos: {passos}")
            return meio
        elif valor_meio < alvo:
            print(f"  → busca na metade direita")
            esquerda = meio + 1
        else:
            print(f"  → busca na metade esquerda")
            direita = meio - 1

    print(f"\nValor {alvo} NÃO encontrado. Total de passos: {passos}")
    return -1

if __name__ == "__main__":
    array = [2, 4, 6, 8, 10, 12, 13]
    alvo = 8

    print(f"Array : {array}")
    print(f"Buscando: {alvo}\n")
    resultado = busca_binaria(array, alvo)
    print(f"\nÍndice do elemento: {resultado}")
