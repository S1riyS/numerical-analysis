import React, { useCallback, useEffect, useRef } from 'react';
import {
    Chart,
    LinearScale,
    PointElement,
    LineElement,
    ScatterController,
    LineController,
    CategoryScale,
    Title,
    Tooltip,
    Legend,
    ChartData,
    ChartOptions,
} from 'chart.js';
import { Point } from '@common/types';

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
    Legend
);

interface FunctionPlotProps {
    func: (x: number) => number;
    minX: number;
    maxX: number;
    step?: number;
    points?: Point[];
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

type CustomChartData = ChartData<'line' | 'scatter', { x: number; y: number }[]>;

const FunctionPlotComponent: React.FC<FunctionPlotProps> = React.memo(({
    func,
    minX,
    maxX,
    step = 0.1,
    points = [],
    width = '100%',
    height = '400px',
    title = 'Function Plot',
    xAxisLabel = 'x',
    yAxisLabel = 'f(x)',
    lineColor = 'rgb(75, 192, 192)',
    pointColor = 'rgb(255, 99, 132)',
    backgroundColor = 'rgba(75, 192, 192, 0.2)',
    gridLines = true,
}) => {
    const chartRef = useRef<HTMLCanvasElement>(null);
    const chartInstance = useRef<Chart<'line' | 'scatter', { x: number; y: number }[], unknown> | null>(null);

    // Memoize the chart data generation
    const generateChartData = useCallback(() => {
        // Generate function data
        const functionData: { x: number; y: number }[] = [];
        for (let x = minX; x <= maxX; x += step) {
            functionData.push({
                x: parseFloat(x.toFixed(4)),
                y: parseFloat(func(x).toFixed(4)),
            });
        }

        // Convert points to numbers
        const pointData: { x: number; y: number }[] = points.map((p) => ({
            x: typeof p.x === 'string' ? parseFloat(p.x) : p.x,
            y: typeof p.y === 'string' ? parseFloat(p.y) : p.y,
        }));

        return {
            datasets: [
                {
                    type: 'line' as const,
                    label: `Function`,
                    data: functionData,
                    borderColor: lineColor,
                    backgroundColor: backgroundColor,
                    borderWidth: 2,
                    pointRadius: 0,
                    tension: 0.1,
                    fill: false,
                },
                {
                    type: 'scatter' as const,
                    label: 'Points',
                    data: pointData,
                    backgroundColor: pointColor,
                    borderColor: pointColor,
                    pointRadius: 3,
                    pointHoverRadius: 4,
                },
            ],
        };
    }, [func, minX, maxX, step, points, lineColor, backgroundColor, pointColor]);

    // Memoize the chart options
    const getChartOptions = useCallback(() => {
        return {
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
                    position: 'top',
                    labels: {
                        usePointStyle: true,
                    },
                },
                tooltip: {
                    callbacks: {
                        label: (context) => {
                            const label = context.dataset.label || '';
                            const value = context.parsed;
                            return `${label}: (${value.x.toFixed(2)}, ${value.y.toFixed(2)})`;
                        },
                    },
                },
            },
            scales: {
                x: {
                    type: 'linear',
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
        } as ChartOptions<'line' | 'scatter'>;
    }, [title, xAxisLabel, yAxisLabel, minX, maxX, gridLines]);

    useEffect(() => {
        if (!chartRef.current) return;

        const ctx = chartRef.current.getContext('2d');
        if (!ctx) return;

        if (chartInstance.current) {
            // Update existing chart
            chartInstance.current.data = generateChartData();
            chartInstance.current.options = getChartOptions();
            chartInstance.current.update();
        } else {
            // Create new chart
            chartInstance.current = new Chart(ctx, {
                type: 'scatter',
                data: generateChartData(),
                options: getChartOptions(),
            });
        }

        return () => {
            if (chartInstance.current) {
                chartInstance.current.destroy();
                chartInstance.current = null;
            }
        };
    }, [generateChartData, getChartOptions]);

    return (
        <div style={{ width, height }}>
            <canvas ref={chartRef} />
        </div>
    );
}, (prevProps, nextProps) => {
    // Custom comparison function - only re-render if these specific props change
    return (
        prevProps.func === nextProps.func &&
        prevProps.width === nextProps.width &&
        prevProps.height === nextProps.height
    );
});

// Export the memoized component
export const FunctionPlot = FunctionPlotComponent;