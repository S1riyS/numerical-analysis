export interface Point {
  x: string;
  y: string;
}

export interface NamedFunction {
  func(x: number): number;
  name: string;
}
