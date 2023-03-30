def chio_method(matrix, factor=1):  # matrix - macierz kwadratowa n x n
    n = len(matrix)

    # szukanie wiersza z niezerowym elementem i zamiana:
    if matrix[0][0] == 0:
        exchange_row = 1
        while matrix[exchange_row][0] == 0 and exchange_row != n:
            exchange_row += 1
        temp = matrix[0]
        matrix[0] = matrix[exchange_row]
        matrix[exchange_row] = temp
        factor *= -1
        
    # tworzenie nowej macierzy o rozmiarze n-1 x n-1
    new_mat = [[0 for i in range(n-1)] for j in range(n-1)]
    for i in range(n-1):
        for j in range(n-1):
            new_mat[i][j] = matrix[0][0] * matrix[i+1][j+1] - matrix[0][j+1] * matrix[i+1][0]
    factor *= 1 / ((matrix[0][0])**(n-2))

    if len(new_mat) == 2:
        det = factor * (new_mat[0][0] * new_mat[1][1] - new_mat[1][0] * new_mat[0][1])
        return det
    else:
        return chio_method(new_mat, factor)

A = [[5 , 1 , 1 , 2 , 3],
[4 , 2 , 1 , 7 , 3],
[2 , 1 , 2 , 4 , 7],
[9 , 1 , 0 , 7 , 0],
[1 , 4 , 7 , 2 , 2]
]
print(chio_method(A))

B =   [[0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]]
print(chio_method(B))
