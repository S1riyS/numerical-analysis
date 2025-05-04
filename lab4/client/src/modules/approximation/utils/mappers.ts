import { ApproximationResult } from "@approximation/api/types";
import { FunctionType } from "@approximation/types";

export function resultToLatex(result: ApproximationResult): string {
    const keysToExtract = ['a', 'b', 'c', 'd'];
    const {a, b, c, d} = keysToExtract.map(key => result.data?.parameters?[key]);
    switch (result.type_) {
        case FunctionType.LINEAR:
            return `${b}x + ${a}`;
        case FunctionType.QUADRATIC:
            return `${c}x^2 + ${b}x + ${a}`;
        case FunctionType.CUBIC:
            return `${d}x^3 + ${c}x^2 + ${b}x + ${a}`;

    }
}