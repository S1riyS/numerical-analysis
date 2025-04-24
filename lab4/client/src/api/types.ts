// src/api/types.ts
export interface Point {
    x: string;
    y: string;
  }
  
  export interface ApiRequest {
    xs: number[];
    ys: number[];
  }
  
  export interface FunctionParameters {
    [key: string]: number;
  }
  
  export interface ApproximationData {
    measure_of_deviation: number;
    mse: number;
    coefficient_of_determination: number;
    parameters: FunctionParameters;
  }
  
  export interface ApproximationResult {
    type_: string;
    success: boolean;
    message: string | null;
    data: ApproximationData;
  }
  
  export interface ApiResponse {
    results: ApproximationResult[];
  }