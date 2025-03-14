def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Matrizes devem ter o mesmo tamanho")

    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha)
    return resultado

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

resultado = soma_matrizes(matriz1, matriz2)
print(resultado)  # Saída: [[6, 8], [10, 12]]