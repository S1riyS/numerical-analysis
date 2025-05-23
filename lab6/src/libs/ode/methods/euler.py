from libs.ode.methods.core.singe_step_method import SingleStepODEMethod


class EulerMethod(SingleStepODEMethod):
    order_of_accuracy = 1

    def _run_method(self) -> None:
        for i in range(1, len(self.xs)):
            y_i = self.ys[i - 1] + self.h * self.f(self.xs[i - 1], self.ys[i - 1])
            self.ys[i] = y_i
