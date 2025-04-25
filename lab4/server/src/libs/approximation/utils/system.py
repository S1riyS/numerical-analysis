import numpy as np

SYSTEM_DECIMAL_PLACES = 5


def solve_system(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    # Solve system with numpy
    solution = np.linalg.solve(A, B)
    # Round solution
    solution = np.round(solution, decimals=SYSTEM_DECIMAL_PLACES)
    # Convert all -0.0 to 0.0
    solution += 0.0

    return solution
