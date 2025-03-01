import numpy as np


def simple_iteration(A, b, tol=1e-10, max_iter=1000):
    """
    Решение СЛАУ методом простых итераций.

    Параметры:
    A: numpy.ndarray - матрица коэффициентов (n x n).
    b: numpy.ndarray - вектор свободных членов (n).
    tol: float - допустимая погрешность (критерий остановки).
    max_iter: int - максимальное число итераций.

    Возвращает:
    x: numpy.ndarray - вектор решения.
    """
    n = len(b)
    x = np.zeros(n)  # Начальное приближение
    D = np.diag(A)  # Диагональные элементы матрицы A
    R = A - np.diagflat(D)  # Остальные элементы матрицы A

    for k in range(max_iter):
        x_new = (b - np.dot(R, x)) / D  # Новое приближение
        if np.linalg.norm(x_new - x) < tol:  # Проверка на сходимость
            print(f"Итерации сошлись на шаге {k+1}")
            return x_new
        x = x_new

    print("Достигнуто максимальное число итераций")
    return x


# Пример использования
A = np.array([[4, 1, 1], [1, 6, -1], [1, 2, 5]], dtype=float)

b = np.array([6, 13, 10], dtype=float)

x = simple_iteration(A, b)
print("Решение:", x)
