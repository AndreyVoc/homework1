def get_matrix(n, m, value):
    matrix = []
    for lin in range(n):
        row = []
        for col in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(2, 2, 10)
print(result1)