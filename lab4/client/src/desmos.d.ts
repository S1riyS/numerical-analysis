import { GraphingCalculator } from '@desmoslabs/desmos';

declare global {
  interface Window {
    Desmos: {
      GraphingCalculator: typeof GraphingCalculator;
    };
  }
}