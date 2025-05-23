import {
  CategoryScale,
  Chart,
  ChartData,
  ChartOptions,
  Legend,
  LineController,
  LineElement,
  LinearScale,
  PointElement,
  ScatterController,
  Title,
  Tooltip,
} from "chart.js";

import React, { useEffect, useRef } from "react";

import { Point } from "@common/types";

// Register necessary Chart.js components
Chart.register(
  LinearScale,
  PointElement,
  LineElement,
  ScatterController,
  LineController,
  CategoryScale,
  Title,
  Tooltip,
  Legend,
);

interface FunctionPlotProps {
  func: (x: number) => number;
  minX: number;
  maxX: number;
  steps?: number;
  points?: Point[];
  singlePoint?: Point;
  width?: string | number;
  height?: string | number;
  title?: string;
  xAxisLabel?: string;
  yAxisLabel?: string;
  lineColor?: string;
  pointColor?: string;
  backgroundColor?: string;
  gridLines?: boolean;
}

type CustomChartData = ChartData<
  "line" | "scatter",
  { x: number; y: number }[]
>;

export const FunctionPlot: React.FC<FunctionPlotProps> = ({
  func,
  minX,
  maxX,
  steps = 1000,
  points = [],
  singlePoint,
  width = "100%",
  height = "400px",
  title = "Function Plot",
  xAxisLabel = "x",
  yAxisLabel = "f(x)",
  lineColor = "rgb(75, 192, 192)",
  pointColor = "rgb(255, 99, 132)",
  backgroundColor = "rgba(75, 192, 192, 0.2)",
  gridLines = true,
}) => {
  const chartRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<Chart<
    "line" | "scatter",
    { x: number; y: number }[],
    unknown
  > | null>(null);

  /**
   * Generates an array of points representing the graph of a given function.
   * The x-values are distributed evenly between minX and maxX.
   *
   * @param f - The mathematical function to plot, which takes a number as input and returns a number.
   * @returns An array of objects, each containing x and y properties, representing points on the function graph.
   */
  function getFunctionData(
    f: (x: number) => number,
  ): { x: number; y: number }[] {
    const functionData: { x: number; y: number }[] = [];
    const stepSize = (maxX - minX) / steps;
    for (let i = 0; i <= steps; i += 1) {
      const xFull = minX + i * stepSize;
      functionData.push({
        x: parseFloat(xFull.toFixed(4)),
        y: parseFloat(f(xFull).toFixed(4)),
      });
    }

    return functionData;
  }

  useEffect(() => {
    if (!chartRef.current) return;

    // Generate function data
    const functionData = getFunctionData(func);

    // Convert points to numbers
    const pointData: { x: number; y: number }[] = points.map((p) => ({
      x: typeof p.x === "string" ? parseFloat(p.x) : p.x,
      y: typeof p.y === "string" ? parseFloat(p.y) : p.y,
    }));

    const ctx = chartRef.current.getContext("2d");
    if (!ctx) return;

    const chartData: CustomChartData = {
      datasets: [
        {
          label: "Function",
          type: "line" as const,
          data: functionData,
          borderColor: lineColor,
          backgroundColor: backgroundColor,
          borderWidth: 2,
          pointRadius: 0,
          tension: 0.1,
          fill: false,
        },
        {
          label: "Points",
          type: "scatter" as const,
          data: pointData,
          backgroundColor: pointColor,
          borderColor: pointColor,
          pointRadius: 3,
          pointHoverRadius: 4,
        },
      ],
    };

    if (singlePoint) {
      chartData.datasets.push({
        label: "Single Point",
        type: "scatter" as const,
        data: [
          {
            x: parseFloat(singlePoint.x),
            y: parseFloat(singlePoint.y),
          },
        ],
        backgroundColor: "rgb(184, 192, 75)",
        borderColor: "rgb(184, 192, 75)",
        pointRadius: 5,
        pointHoverRadius: 6,
      });
    }

    const chartOptions: ChartOptions<"line" | "scatter"> = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: false,
          text: title,
          font: {
            size: 16,
          },
        },
        legend: {
          position: "top",
          labels: {
            usePointStyle: true,
          },
        },
        tooltip: {
          callbacks: {
            label: (context) => {
              const label = context.dataset.label || "";
              const value = context.parsed;
              return `${label}: (${value.x.toFixed(2)}, ${value.y.toFixed(2)})`;
            },
          },
        },
      },
      scales: {
        x: {
          type: "linear",
          title: {
            display: true,
            text: xAxisLabel,
          },
          min: minX,
          max: maxX,
          grid: {
            display: gridLines,
          },
        },
        y: {
          title: {
            display: true,
            text: yAxisLabel,
          },
          grid: {
            display: gridLines,
          },
        },
      },
    };

    if (chartInstance.current) {
      // Update existing chart
      chartInstance.current.data = chartData;
      chartInstance.current.options = chartOptions;
      chartInstance.current.update();
    } else {
      // Create new chart
      chartInstance.current = new Chart(ctx, {
        type: "scatter",
        data: chartData,
        options: chartOptions,
      });
    }

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
        chartInstance.current = null;
      }
    };
  }, [func]);

  return (
    <div style={{ width, height }}>
      <canvas ref={chartRef} />
    </div>
  );
};
