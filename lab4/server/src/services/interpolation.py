import sympy as sp  # type: ignore
from libs.interpolation.methods import (
    LagrangeSolver,
    NewtonDividedDifferencesSolver,
    NewtonFiniteDifferencesSolver,
)
from libs.interpolation.methods.core.base_point_solver import BasePointSolver
from libs.interpolation.methods.core.base_solver import BaseSolver
from libs.interpolation.methods.core.enums import (
    InterpolationMethod,
    PointInterpolationMethod,
)
from libs.interpolation.methods.stirling_point import StirlingSolver
from schemas.interpolation import (
    InterpolationData,
    InterpolationRequest,
    InterpolationResponse,
    PointInterpolationData,
    PointInterpolationRequest,
    PointInterpolationResponse,
)

x = sp.symbols("x")


class InterpolationService:
    async def interpolate(self, data: InterpolationRequest) -> InterpolationResponse:
        solver: BaseSolver | None = None

        if data.method == InterpolationMethod.NEWTON_DIVIDED_DIFFERENCES:
            solver = NewtonDividedDifferencesSolver(
                data.points.xs, data.points.ys, data.x_value
            )
        elif data.method == InterpolationMethod.NEWTON_FINITE_DIFFERENCES:
            solver = NewtonFiniteDifferencesSolver(
                data.points.xs, data.points.ys, data.x_value
            )
        elif data.method == InterpolationMethod.LAGRANGE:
            solver = LagrangeSolver(data.points.xs, data.points.ys, data.x_value)

        if not solver:
            raise Exception("Invalid interpolation method")

        validation_res = solver.validate()
        res_data: InterpolationData | None = None
        if validation_res.success:
            res = solver.solve()
            f_expr = round_expr(res.expr)
            res_data = InterpolationData(f_expr=f_expr, y_value=res.y_value)

        return InterpolationResponse(
            method=solver.interpolation_method,
            points=data.points,
            x_value=data.x_value,
            success=validation_res.success,
            message=validation_res.message,
            data=res_data,
        )

    async def point_interpolate(
        self, data: PointInterpolationRequest
    ) -> PointInterpolationResponse:
        solver: BasePointSolver | None = None

        if data.method == PointInterpolationMethod.STIRLING:
            solver = StirlingSolver(data.points.xs, data.points.ys, data.x_value)

        if not solver:
            raise Exception("Invalid interpolation method")

        validation_res = solver.validate()
        res_data: PointInterpolationData | None = None
        if validation_res.success:
            res = solver.solve()
            f_expr = round_expr(res.expr)
            res_data = PointInterpolationData(f_expr=f_expr, y_value=res.y_value)

        return PointInterpolationResponse(
            method=solver.point_interpolation_method,
            points=data.points,
            x_value=data.x_value,
            success=validation_res.success,
            message=validation_res.message,
            data=res_data,
        )


def round_expr(expr: sp.Expr, n: int = 10) -> str:
    def round_floats(x):
        if isinstance(x, sp.Float):
            return sp.Float(round(x, n))
        elif isinstance(x, sp.core.numbers.Integer):
            return x
        elif isinstance(
            x,
            (
                sp.core.numbers.Rational,
                sp.core.numbers.Pi,
                sp.core.numbers.E,
                sp.core.numbers.EulerGamma,
            ),
        ):
            return x
        elif isinstance(x, sp.core.power.Pow):
            return x.func(round_floats(x.base), x.exp)
        return x

    # Create a mapping of all float numbers to their rounded versions
    mapping = {x: round_floats(x) for x in expr.atoms(sp.Float)}

    # Substitute all floats in the expression with their rounded versions
    rounded_expr = expr.subs(mapping)

    return str(rounded_expr)
