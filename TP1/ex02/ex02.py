import random

NOMES = {1: "Ás", 11: "Valete", 12: "Dama", 13: "Rei"}

def nome_carta(valor):
    return NOMES.get(valor, str(valor))

def insertion_sort_cartas(cartas: list) -> list:
    """
    Ordena as cartas simulando o processo descrito no enunciado.
    cartas: lista de inteiros (1=Ás, 2..10, 11=Valete, 12=Dama, 13=Rei)
    Retorna: nova lista ordenada
    """
    cartas = cartas[:]  # Cópia para não modificar a original

    for i in range(1, len(cartas)):
        carta_na_mao = cartas[i]   # Carta retirada da pilha (mão direita)
        j = i - 1

        # Empurra cartas maiores para a direita para abrir espaço
        while j >= 0 and cartas[j] > carta_na_mao:
            cartas[j + 1] = cartas[j]
            j -= 1

        cartas[j + 1] = carta_na_mao  # Insere na posição correta
        print(f"  Inseriu '{nome_carta(carta_na_mao)}' → {[nome_carta(c) for c in cartas[:i+1]]}")

    return cartas

if __name__ == "__main__":
    espadas = list(range(1, 14))
    random.shuffle(espadas)

    print("Cartas embaralhadas:", [nome_carta(c) for c in espadas])
    print("\nProcesso de ordenação:")
    ordenadas = insertion_sort_cartas(espadas)
    print("\nCartas ordenadas   :", [nome_carta(c) for c in ordenadas])
