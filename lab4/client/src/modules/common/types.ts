export interface Point {
    x: number | string;
    y: number | string;
}

export interface NamedFunction {
    func(x: number): number
    name: string
}