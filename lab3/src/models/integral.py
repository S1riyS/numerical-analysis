from typing import List

import sympy as sp  # type: ignore
from sympy.abc import x  # type: ignore

from logger import GlobalLogger
from models.discontinuity import Discontinuity, DiscontinuityKind

logger = GlobalLogger()


class Integral:
    def __init__(self, function_str: str, left: float, right: float):
        self.function_str = function_str
        self.f = self.__validate_and_parse_function(function_str)
        self.left = left
        self.right = right

    def __validate_and_parse_function(self, function_str: str) -> sp.Lambda:
        # Replace commas and "^" representation of power function
        function_str = function_str.replace(",", ".").replace("^", "**")

        # Try parsing function
        try:
            logger.debug(f"Trying to parse function: {function_str}")
            expr = sp.sympify(function_str)
        except sp.SympifyError:
            raise ValueError("Invalid function format")

        # Make sure that only "x" variable is used
        used_symbols = expr.free_symbols
        if len(used_symbols) != 1 and used_symbols[0] != x:
            raise ValueError(f"Only 'x' variable is allowed! Check function")

        # Parse expression to function
        func = sp.Lambda(x, expr)
        return func

    def find_discontinuities(self) -> List[Discontinuity]:
        """
        Identifies discontinuities in the integral's function within the specified interval.

        This function evaluates the mathematical expression of the function to find potential
        points of discontinuity within the given interval [left, right]. It investigates points
        where the function is undefined, such as zero denominators and non-positive arguments
        of logarithms, and then determines the type of discontinuity at each critical point.

        Returns:
            List[Discontinuity]: A list of `Discontinuity` objects, each representing a point
            of discontinuity within the interval. Discontinuities are classified into types
            such as REMOVABLE, JUMP, or ESSENTIAL.
        """

        discontinuities = []
        expr = self.f(x)
        search_domain = sp.Interval(self.left, self.right)

        # Find points where the function is potentially discontinuous
        # 1. Points where the function is undefined (e.g., denominator zero)
        denominator = expr.as_numer_denom()[1]
        critical_points = sp.solveset(sp.Eq(denominator, 0), x, domain=search_domain)

        # 2. Points where the argument of the logarithm is non-positive
        # Traverse the expression tree to find logarithms
        for sub_expr in sp.preorder_traversal(expr):
            if isinstance(sub_expr, sp.log):
                log_arg = sub_expr.args[0]
                # Find points where log_arg <= 0
                critical_points = critical_points.union(sp.solveset(sp.Eq(log_arg, 0), x, domain=search_domain))
                critical_points = critical_points.union(sp.solveset(log_arg < 0, x, domain=search_domain))

        # Check each critical point
        for point in critical_points:
            if not point.is_Float and not point.is_Integer:
                # Try to evaluate numerically if symbolic
                try:
                    point_eval = point.evalf()
                    if point_eval.is_real and self.left <= float(point_eval) <= self.right:
                        point = point_eval
                    else:
                        continue
                except:
                    continue

            # Check left and right limits
            try:
                left_limit = sp.limit(expr, x, point, dir="-")
                right_limit = sp.limit(expr, x, point, dir="+")
                limit_exists = left_limit == right_limit and left_limit.is_finite
            except:
                # If limit calculation fails, assume essential
                discontinuities.append(Discontinuity(point, DiscontinuityKind.ESSENTIAL))
                continue

            if limit_exists:
                discontinuities.append(Discontinuity(point, DiscontinuityKind.REMOVABLE))

                # Add piecewise function to handle removable discontinuity
                # f_new(point) = limit, f_new(x) = f(x)
                expr = sp.Piecewise(
                    (left_limit, sp.Eq(x, point)),
                    (expr, True),
                )
                self.f = sp.Lambda(x, expr)

            else:
                if left_limit.is_finite and right_limit.is_finite:
                    discontinuities.append(Discontinuity(point, DiscontinuityKind.JUMP))
                else:
                    discontinuities.append(Discontinuity(point, DiscontinuityKind.ESSENTIAL))

        return discontinuities

    def __str__(self) -> str:
        return f"{self.function_str} from {self.left} to {self.right}"
