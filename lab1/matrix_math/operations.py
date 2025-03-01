def dot_product(v1, v2):
    """
    Вычисляет скалярное произведение двух векторов.
    """
    return sum(x * y for x, y in zip(v1, v2))


def matrix_vector_multiply(matrix, vector):
    """
    Умножает матрицу на вектор.
    """
    return [dot_product(row, vector) for row in matrix]


def subtract_vectors(v1, v2):
    """
    Вычитает два вектора.
    """
    return [x - y for x, y in zip(v1, v2)]


def add_vectors(v1, v2):
    """
    Суммирует два вектора.
    """
    return [x + y for x, y in zip(v1, v2)]


def vector_norm(vector):
    """
    Вычисляет норму вектора.
    """
    return max(abs(x) for x in vector)


def matrix_norm(A):
    return max(sum(abs(x) for x in row) for row in A)


def get_diagonal(matrix):
    """
    Возвращает диагональные элементы матрицы.
    """
    return [matrix[i][i] for i in range(len(matrix))]


def subtract_matrices(A, B):
    """
    Вычитает две матрицы.
    """
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
