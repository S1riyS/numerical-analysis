from libs.ode.methods.core.enums import ODEMethodType
from libs.ode.methods.euler import EulerMethod
from schemas.ode import ODERequestSchema


def main() -> None:
    request = ODERequestSchema(
        x0=1.0,
        xn=10,
        y0=-1,
        f=lambda x, y: y + (1 + x) * y**2,
        N=3,
        eps=1e-3,
        method=ODEMethodType.EULER,
    )

    method = EulerMethod(request, max_N=1000)
    # method = RungeKutta4OrderMethod(request)

    solution = method.solve()
    print(solution.xs)
    print(solution.ys)
    print(len(solution.xs))


if __name__ == "__main__":
    main()
