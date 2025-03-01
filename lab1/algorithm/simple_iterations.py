from cli.console.printer import Printer
from matrix_math.operations import (
    add_vectors,
    matrix_norm,
    matrix_vector_multiply,
    subtract_vectors,
    vector_norm,
)


def split_matrix(matrix):
    A = [row[:-1] for row in matrix]  # Все столбцы, кроме последнего
    b = [row[-1] for row in matrix]  # Последний столбец
    return A, b


def diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= sum_row:
            return False
    return True


def rearrange_for_diagonal_dominance(A, b):
    n = len(A)
    for i in range(n):
        max_index = i
        max_value = abs(A[i][i])
        for j in range(i + 1, n):
            if abs(A[j][i]) > max_value:
                max_index = j
                max_value = abs(A[j][i])
        if max_index != i:
            A[i], A[max_index] = A[max_index], A[i]
            b[i], b[max_index] = b[max_index], b[i]
    return A, b


def simple_iteration_method(A, b, eps, max_iterations=1000):
    n = len(A)

    # Создаем матрицу C
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = -A[i][j] / A[i][i]

    Printer.success(f"Норма матрицы C: {matrix_norm(C)}")

    # Создаем вектор d
    d = [0 for _ in range(n)]
    for i in range(n):
        d[i] = b[i] / A[i][i]

    x = [0 for _ in range(n)]  # Начальное приближение
    x_next = [0 for _ in range(n)]  # Слудующее приближение

    # Выполняем итерации
    for iteration in range(max_iterations):
        x_next = matrix_vector_multiply(C, x)
        x_next = add_vectors(x_next, d)

        # Проверка на достижение точности
        error = vector_norm(subtract_vectors(x_next, x))
        if error < eps:
            return x_next, iteration + 1, error

        x = x_next.copy()

    return x, max_iterations, error


def solve(matrix: list[list[float]], eps: float):
    # Разделение матрицы на A и b
    A, b = split_matrix(matrix)

    # Проверка диагонального преобладания
    if not diagonal_dominance(A):
        Printer.warning("Диагональное преобладание отсутствует. Пытаемся переставить строки...")
        A, b = rearrange_for_diagonal_dominance(A, b)
        if not diagonal_dominance(A):
            Printer.error("Невозможно достичь диагонального преобладания.")
            return

    x, iterations, error = simple_iteration_method(A, b, eps)

    # Вывод результатов
    Printer.success(f"Вектор неизвестных:")
    for value in x:
        Printer.default(value)
    Printer.success(f"Количество итераций: {iterations}")
    Printer.success(f"Норма погрешности: {error}")
