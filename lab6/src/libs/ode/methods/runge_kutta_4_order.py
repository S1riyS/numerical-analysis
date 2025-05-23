from libs.ode.methods.core.singe_step_method import SingleStepODEMethod


class RungeKutta4OrderMethod(SingleStepODEMethod):
    order_of_accuracy = 4

    def _run_method(self) -> None:
        for i in range(1, len(self.xs)):
            k1 = self.h * self.f(self.xs[i - 1], self.ys[i - 1])
            k2 = self.h * self.f(self.xs[i - 1] + self.h / 2, self.ys[i - 1] + k1 / 2)
            k3 = self.h * self.f(self.xs[i - 1] + self.h / 2, self.ys[i - 1] + k2 / 2)
            k4 = self.h * self.f(self.xs[i - 1] + self.h, self.ys[i - 1] + k3)

            next_y = self.ys[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            self.ys[i] = next_y
