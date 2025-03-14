def cria_matriz(l, c):
    m = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(f'digite o elemento m[{j}][{i}]: ')))
        m.append(linha)
    return m

def printa_matriz(matriz):
    for i in matriz:
        for j in i:
          print(j, end= '')
        print()

matriz = cria_matriz(2, 2)
printa_matriz(matriz)