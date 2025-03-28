import tkinter as tk
from decimal import getcontext
from tkinter import ttk
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Converters
from converters.dec import convert2decimal
from converters.float import convert2float

# Equation
from equation.data import equation_methods, equations
from equation.methods import ChordMethod, EquationNewtonMethod, SimpleIterationsMethod
from equation.methods_enum import EquationMethod
from equation.model import Equation

# System
from system.data import system_methods, systems
from system.methods import SystemNewtonMethod
from system.methods_enum import SystemMethod
from system.model import System


class MathSolverApp:
    __RESULT_PREFIX = "Результат:\n"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Лабораторная работа №2")

        # Создание графика
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Создание вкладок
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Вкладка для одного уравнения
        self.equation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.equation_frame, text="Нелинейное уравнение")

        # Вкладка для системы уравнений
        self.system_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.system_frame, text="Система нелинейных уравнений")

        # Панель результатов
        self.result_frame = ttk.Frame(root)
        self.result_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.result_label = ttk.Label(self.result_frame, text="Результат: ")
        self.result_label.pack(side=tk.LEFT, padx=5, pady=5)

        # Данные для решения уравнения:
        self.chosen_equation: Optional[Equation] = None
        self.chosen_equation_method: Optional[EquationMethod] = None

        # Данные для решения системы:
        self.chosen_system: Optional[System] = None
        self.chosen_system_method: Optional[SystemMethod] = None

        # Инициализация вкладок
        self.__init_equation_tab()
        self.__init_system_tab()

    def __init_equation_tab(self):
        # Выбор уравнения
        ttk.Label(self.equation_frame, text="Уравнение").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.equation_var = tk.StringVar()
        self.equation_combobox = ttk.Combobox(self.equation_frame, textvariable=self.equation_var)
        self.equation_combobox["values"] = [str(equation) for equation in equations]
        self.equation_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew", columnspan=2)
        self.equation_combobox.bind("<<ComboboxSelected>>", self.__on_equation_select)

        # Выбор метода решения
        ttk.Label(self.equation_frame, text="Метод решения").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.method_var = tk.StringVar()
        self.equation_method_combobox = ttk.Combobox(self.equation_frame, textvariable=self.method_var)
        self.equation_method_combobox["values"] = [str(method) for method in equation_methods]
        self.equation_method_combobox.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="ew")
        self.equation_method_combobox.bind("<<ComboboxSelected>>", self.__on_equation_method_select)

        # Ввод границ и точности
        ttk.Label(self.equation_frame, text="Левая граница").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.left_bound = ttk.Entry(self.equation_frame)
        self.left_bound.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.equation_frame, text="Правая граница").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.right_bound = ttk.Entry(self.equation_frame)
        self.right_bound.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.equation_frame, text="Точность").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.equation_precision = ttk.Entry(self.equation_frame)
        self.equation_precision.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Кнопка решения
        self.solve_button = ttk.Button(
            self.equation_frame,
            text="Решить",
            command=self.__solve_equation,
        )
        self.solve_button.grid(row=5, column=0, ipadx=70, columnspan=2, pady=10)

    def __init_system_tab(self):
        # Выбор уравнения
        ttk.Label(self.system_frame, text="Система").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.system_var = tk.StringVar()
        self.system_combobox = ttk.Combobox(self.system_frame, textvariable=self.system_var)
        self.system_combobox["values"] = [str(system) for system in systems]
        self.system_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew", columnspan=2)
        self.system_combobox.bind("<<ComboboxSelected>>", self.__on_system_select)

        # Выбор метода решения для системы
        ttk.Label(self.system_frame, text="Метод решения").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.system_method_var = tk.StringVar()
        self.system_method_combobox = ttk.Combobox(self.system_frame, textvariable=self.system_method_var)
        self.system_method_combobox["values"] = [str(method) for method in system_methods]
        self.system_method_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.system_method_combobox.bind("<<ComboboxSelected>>", self.__on_system_method_select)

        # Начальное приближение X и Y
        ttk.Label(self.system_frame, text="Начальное приближение X").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.initial_x = ttk.Entry(self.system_frame)
        self.initial_x.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.system_frame, text="Начальное приближение Y").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.initial_y = ttk.Entry(self.system_frame)
        self.initial_y.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.system_frame, text="Точность").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.system_precision = ttk.Entry(self.system_frame)
        self.system_precision.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Кнопка решения для системы
        self.solve_system_button = ttk.Button(self.system_frame, text="Решить", command=self.__solve_system)
        self.solve_system_button.grid(row=5, column=0, ipadx=70, columnspan=2, pady=10)

    def __solve_equation(self):
        # Получить значения из полей ввода
        try:
            if self.chosen_equation is None or self.chosen_equation_method is None:
                raise ValueError

            left = convert2float(self.left_bound.get())
            right = convert2float(self.right_bound.get())
            epsilon = convert2decimal(self.equation_precision.get())

            if left >= right:
                raise ValueError

        except Exception:
            self.__set_result("Введены некорректные данные")
            return

        # Рисуем график
        try:
            x = np.linspace(left, right, 400)
            y = list(map(self.chosen_equation.function, x))

            self.ax.clear()

            self.ax.axhline(y=0, color="gray")
            self.ax.axvline(x=0, color="gray")
            self.ax.plot(x, y)

            self.ax.relim()  # Пересчет границ данных
            self.ax.autoscale()  # Автоматическое масштабирование осей
            self.ax.grid(True)

            self.ax.set_title("График функции")
            self.canvas.draw()
        except Exception:
            self.__set_result("Не удалось отрисовать график")
            return

        # Выбираем метод решения
        method = None
        if self.chosen_equation_method == EquationMethod.CHORD:
            method = ChordMethod(self.chosen_equation, left, right, epsilon, 10, False)
        elif self.chosen_equation_method == EquationMethod.NEWTON:
            method = EquationNewtonMethod(self.chosen_equation, left, right, epsilon, 10, False)
        elif self.chosen_equation_method == EquationMethod.SIMPLE_ITERATIONS:
            method = SimpleIterationsMethod(self.chosen_equation, left, right, epsilon, 10, False)

        # Обновление результата
        if method is None:
            self.__set_result("Метод решения не удалось применить")
            return

        has_root, message = method.check()
        if not has_root:
            self.__set_result(message)
            return
        try:
            result = method.solve()
            self.__set_result(str(result))
            self.ax.scatter(result.root, result.function_value_at_root, color="red", s=20, zorder=3)
            self.canvas.draw()

        except Exception as e:
            self.__set_result("Не удалось решить уравнение")
            print(e.with_traceback())

    def __solve_system(self):
        # Получить значения из полей ввода
        try:
            if self.chosen_system is None or self.chosen_system_method is None:
                raise ValueError

            x0 = convert2float(self.initial_x.get())
            y0 = convert2float(self.initial_y.get())
            epsilon = convert2decimal(self.system_precision.get())
        except ValueError:
            self.__set_result("Введены некорректные данные")
            return

        # Выбираем метод решения
        method = None
        if self.chosen_system_method == SystemMethod.NEWTON:
            method = SystemNewtonMethod(self.chosen_system, x0, y0, epsilon, 10)

        # Обновление результата
        if method is None:
            self.__set_result("Метод решения не удалось применить")
            return

        try:
            result = method.solve()
            self.__set_result(str(result))
        except Exception as e:
            self.__set_result("Не удалось решить систему")
            return

        # Рисуем график
        try:
            x = np.linspace(result.root_x - 3, result.root_x + 3, 400)
            y = np.linspace(result.root_y - 3, result.root_y + 3, 400)
            X, Y = np.meshgrid(x, y)

            Z1 = self.chosen_system.f1(X, Y)
            Z2 = self.chosen_system.f2(X, Y)

            self.ax.clear()
            self.ax.contour(X, Y, Z1, levels=[0], colors="blue")
            self.ax.contour(X, Y, Z2, levels=[0], colors="yellow")
            self.ax.scatter(result.root_x, result.root_y, color="red", s=20, zorder=3)

            # self.ax.relim()  # Пересчет границ данных
            # self.ax.autoscale()  # Автоматическое масштабирование осей
            self.ax.grid(True)

            self.ax.set_title("График функции")
            self.canvas.draw()
        except Exception:
            self.__set_result("Не удалось отрисовать график")
            return

    def __set_result(self, message: str) -> None:
        self.result_label.config(text=MathSolverApp.__RESULT_PREFIX + message)

    def __on_equation_select(self, event) -> None:
        selected_index = self.equation_combobox.current()
        if selected_index >= 0:
            self.chosen_equation = equations[selected_index]

    def __on_equation_method_select(self, event) -> None:
        selected_index = self.equation_method_combobox.current()
        if selected_index >= 0:
            self.chosen_equation_method = equation_methods[selected_index]

    def __on_system_select(self, event) -> None:
        selected_index = self.system_combobox.current()
        if selected_index >= 0:
            self.chosen_system = systems[selected_index]

    def __on_system_method_select(self, event) -> None:
        selected_index = self.system_method_combobox.current()
        if selected_index >= 0:
            self.chosen_system_method = system_methods[selected_index]


if __name__ == "__main__":
    getcontext().prec = 100  # Кол-во знаков после запятой
    root = tk.Tk()
    app = MathSolverApp(root)
    root.mainloop()
