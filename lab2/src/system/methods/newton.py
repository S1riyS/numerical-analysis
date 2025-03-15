import numpy as np
from scipy.optimize import approx_fprime  # type: ignore

from system.methods.method import ISystemMethod  # type: ignore
from system.result import SystemResult  # type: ignore


class NewtonMethod(ISystemMethod):
    __MAX_ITER = 10_000

    def __compute_jacobian(self, x: float, y: float):
        f1, f2 = self.system.f1, self.system.f2

        # Вычисляем частные производные для f1
        df1_dx = approx_fprime(np.array([x, y]), lambda v: f1(v[0], v[1]))[0]
        df1_dy = approx_fprime(np.array([x, y]), lambda v: f1(v[0], v[1]))[1]

        # Вычисляем частные производные для f2
        df2_dx = approx_fprime(np.array([x, y]), lambda v: f2(v[0], v[1]))[0]
        df2_dy = approx_fprime(np.array([x, y]), lambda v: f2(v[0], v[1]))[1]

        # Возвращаем матрицу Якоби
        return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])

    def solve(self) -> SystemResult:
        f1, f2 = self.system.f1, self.system.f2
        x, y = self.x0, self.y0

        for iteration in range(1, NewtonMethod.__MAX_ITER + 1):
            # Вычисляем значения функций
            f1_val = f1(x, y)
            f2_val = f2(x, y)

            # Вычисляем матрицу Якоби
            J = self.__compute_jacobian(x, y)

            # Вычисляем вектор правой части
            F = np.array([-f1_val, -f2_val])

            # Решаем систему линейных уравнений
            delta = np.linalg.solve(J, F)

            # Обновляем значения x и y
            x += delta[0]
            y += delta[1]

            # Проверяем условие сходимости
            if np.linalg.norm(delta) < self.epsilon:
                return SystemResult(x, y, iteration, self.decimal_places)

        print("Метод не сошелся за максимальное число итераций.")
        return None
