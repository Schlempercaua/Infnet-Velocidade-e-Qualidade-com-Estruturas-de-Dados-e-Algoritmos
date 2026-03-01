import math

def quadrado_do_arroz(graos: int) -> int:
    """
    Retorna em qual quadrado do tabuleiro colocar a quantidade de grãos.
    
    Complexidade: O(1) — Tempo Constante
    """
    if graos < 1:
        raise ValueError("O número de grãos deve ser pelo menos 1.")

    log = math.log2(graos)

    if not log.is_integer():
        raise ValueError(f"{graos} não é uma potência de 2. "
                         f"Use: 1, 2, 4, 8, 16, 32, 64, ...")

    quadrado = int(log) + 1

    if quadrado > 64:
        raise ValueError(f"O tabuleiro tem apenas 64 quadrados. "
                         f"{graos} grãos excedem o limite.")

    """Alguns tratamentos basicos para garantir que a função funcione corretamente"""   
    
    return quadrado

# Função inversa: dado o quadrado, retorna os grãos

def graos_no_quadrado(quadrado: int) -> int:
    """Retorna quantos grãos há em determinado quadrado. O(1)"""
    if not 1 <= quadrado <= 64:
        raise ValueError("O quadrado deve estar entre 1 e 64.")
    return 2 ** (quadrado - 1)


if __name__ == "__main__":
    print("=== Tabela: Quadrado x Grãos ===")
    print(f"{'Quadrado':>10} | {'Grãos':>20}")
    print("-" * 35)
    for q in range(1, 11):  # Primeiros 10 quadrados
        print(f"{q:>10} | {graos_no_quadrado(q):>20,}")

    print("\n=== Testes da função quadrado_do_arroz ===")
    testes = [1, 2, 4, 8, 16, 32, 64, 128, 1024]
    for graos in testes:
        q = quadrado_do_arroz(graos)
        print(f"  {graos:>6} grãos → quadrado {q}")

    print("\n=== Big O da função ===")
    print("Complexidade de Tempo: O(1) — Constante")
    print("A função executa math.log2() + int() + soma: sempre 3 operações.")
    print("Não importa se entrada é 16 ou 2 elevado a63: mesmo custo computacional.")
