import { ApproximationResponse } from "@approximation/api/types";
import { FunctionType } from "@approximation/types";

export function getBestApproximationType(response: ApproximationResponse): FunctionType | null {
    const validResults = response.results.filter(
      r => r.success && r.data?.mse !== undefined
    );
  
    if (!validResults.length) return null;
  
    const bestResult = validResults.reduce((best, current) => 
      current.data!.mse! < best.data!.mse! ? current : best
    );
  
    return bestResult.type_;
  }