class ArrayBubble:
    def __init__(self, arr):
        self.__a = arr[:]
        self.__nItems = len(arr)

    def swap(self, i, j):
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def bubbleSort(self):
        esquerda = 0
        direita = self.__nItems - 1

        while esquerda < direita:

            # Esquerda para direita: leva o MAIOR para a direita
            for inner in range(esquerda, direita):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)
            direita -= 1

            # Direita para esquerda: leva o MENOR para a esquerda
            for inner in range(direita, esquerda, -1):
                if self.__a[inner] < self.__a[inner - 1]:
                    self.swap(inner, inner - 1)
            esquerda += 1

    def display(self):
        print(self.__a)

arr = ArrayBubble([64, 34, 25, 12, 22, 11, 90])
arr.display()   # Antes
arr.bubbleSort()
arr.display()   # Depois