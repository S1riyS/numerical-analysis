import { FunctionType } from "@approximation/types";

export interface AnalysisResult {
    type_: FunctionType;
    success: boolean;
    message: string | null;
    data: {
      measure_of_deviation?: number;
      mse?: number;
      coefficient_of_determination?: number;
      parameters?: Record<string, number>;
    } | null;
  }
  
  export interface AnalysisResponse {
    results: AnalysisResult[];
  }