import { BigNumber, MathNode, isFunctionNode, isSymbolNode } from "mathjs";

import { configuredMath } from "./mathjs";

const allowedVariables = new Set(["x"]);
const allowedConstants = new Set(["e", "pi"]);
const knownFunctions = new Set(["log", "sin", "cos", "tan", "sqrt", "abs"]);
export function fExprToFunction(fExpr: string): (x: number) => number {
  try {
    fExpr = fExpr
      .replace(/\*\*/g, "^")
      .replace(/\bln\(/g, "log(")
      .replace(/\be\b/g, "e");

    const node = configuredMath.parse(fExpr);

    // Collect symbols used as variables
    const invalidSymbols = new Set<string>();

    node.traverse((n: MathNode, _, parent) => {
      if (isSymbolNode(n)) {
        const name = n.name;

        // If it's a function, ensure it's being *called* (i.e., parent is FunctionNode)
        const isFunction = knownFunctions.has(name);
        const isProperCall = isFunctionNode(parent) && parent.fn.name === name;

        if (
          !allowedVariables.has(name) &&
          !allowedConstants.has(name) &&
          !(isFunction && isProperCall)
        ) {
          invalidSymbols.add(name);
        }
      }
    });

    if (invalidSymbols.size > 0) {
      // console.error(`Disallowed symbol(s): ${Array.from(invalidSymbols).join(", ")}`);
      return null;
    }

    return (x: number) => {
      return node.evaluate({ x });
    };
  } catch {
    // console.error("Invalid math expression:", fExpr, err);
    return null;
  }
}

export function isStrictFloat(str: string): boolean {
  return /^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$/.test(str.trim());
}

export function hydrateFExpr(
  fExpr: string,
  parameters: Record<string, string>,
  precision?: number,
): string {
  Object.entries(parameters).forEach(([key, value]) => {
    fExpr = fExpr.replace(key, precision ? (+value).toFixed(precision) : value);
  });
  return fExpr;
}

export function fExprToKatex(fExpr: string): string {
  return fExpr
    .replace(/([0-9.]+)e([+-]?[0-9]+)/gi, (_, base, exp) => {
      return `${base}\\cdot 10^{${exp}}`;
    })
    .replace(/\*\*/g, "^")
    .replace(/\^(\d{2,})/g, "^($1)")
    .replace(/\*/g, "\\cdot ")
    .replace(/\+\s*-/g, "-")
    .replace(/\(/g, "{")
    .replace(/\)/g, "}");
}
