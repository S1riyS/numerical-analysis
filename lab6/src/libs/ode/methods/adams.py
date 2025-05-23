from libs.ode.methods.core.enums import ODEMethodType
from libs.ode.methods.core.multi_step_method import MultiStepODEMethod
from libs.ode.methods.euler import EulerMethod
from schemas.ode import ODERequestSchema


class AdamsMethod(MultiStepODEMethod):
    def _run_method(self) -> None:
        euler_request = ODERequestSchema(
            x0=self.x0,
            xn=self.xn,
            y0=self.y0,
            f=self.f,
            N=self.N,
            eps=float("inf"),  # We need 1 iteration of Euler method
            method=ODEMethodType.EULER,
        )
        euler_response = EulerMethod(euler_request, max_N=self._max_N).solve()
        self.ys[:4] = euler_response.ys[:4]

        for i in range(4, self.N):
            f_i_1 = self.f(self.xs[i - 1], self.ys[i - 1])
            f_i_2 = self.f(self.xs[i - 2], self.ys[i - 2])
            f_i_3 = self.f(self.xs[i - 3], self.ys[i - 3])
            f_i_4 = self.f(self.xs[i - 4], self.ys[i - 4])

            df_1 = f_i_1 - f_i_2
            df_2 = f_i_1 - 2 * f_i_2 + f_i_3
            df_3 = f_i_1 - 3 * f_i_2 + 3 * f_i_3 - f_i_4

            next_y = self.ys[i - 1]
            next_y += self.h * f_i_1
            next_y += ((self.h**2) / 2) * df_1
            next_y += ((5 * self.h**3) / 12) * df_2
            next_y += ((3 * self.h**4) / 8) * df_3

            self.ys[i] = next_y
