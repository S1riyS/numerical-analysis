import { ApproximationResult } from "@approximation/api/types";
import { FunctionType } from "@approximation/types";

function signed(x: number): string {
  if (x >= 0) return `+${x}`;
  return `-${-x}`;
}

export function resultToLatex(result: ApproximationResult): string {
  // Check if data and parameters exist
  if (!result.data || !result.data.parameters) {
    return "undefined";
  }

  const { a, b, c, d } = result.data.parameters;
  switch (result.type_) {
    case FunctionType.LINEAR:
      return `${b}x ${signed(a)}`;
    case FunctionType.QUADRATIC:
      return `${c}x^2 ${signed(b)}x ${signed(a)}`;
    case FunctionType.CUBIC:
      return `${d}x^3 ${signed(c)}x^2 ${signed(b)}x ${signed(a)}`;
    case FunctionType.EXPONENTIAL:
      return `${a} \\cdot e^{${b}x}`;
    case FunctionType.LOGARITHMIC:
      return `${a} ${signed(b)} \\cdot \\log(x)`;
    case FunctionType.POWER:
      return `${a} \\cdot x^{${b}}`;
  }
}

export function resultToFunction(
  result: ApproximationResult,
): (a: number) => number {
  // Check if data and parameters exist
  if (!result.data || !result.data.parameters) {
    return (_) => 0;
  }

  const { a, b, c, d } = result.data.parameters;
  switch (result.type_) {
    case FunctionType.LINEAR:
      return (x) => b * x + a;
    case FunctionType.QUADRATIC:
      return (x) => c * x ** 2 + b * x + a;
    case FunctionType.CUBIC:
      return (x) => d * x ** 3 + c * x ** 2 + b * x + a;
    case FunctionType.EXPONENTIAL:
      return (x) => a * Math.E ** (b * x);
    case FunctionType.LOGARITHMIC:
      return (x) => a + b * Math.log(x);
    case FunctionType.POWER:
      return (x) => a * x ** b;
  }
}

export function typeToName(type_: FunctionType): string {
  switch (type_) {
    case FunctionType.LINEAR:
      return "Линейная";
    case FunctionType.QUADRATIC:
      return "Квадратичная";
    case FunctionType.CUBIC:
      return "Кубическая";
    case FunctionType.EXPONENTIAL:
      return "Экспонента";
    case FunctionType.LOGARITHMIC:
      return "Логарифм";
    case FunctionType.POWER:
      return "Степенная";
  }
}
