from typing import List

from libs.approximation.methods import approximation_methods
from libs.approximation.utils.statistic import (
    compute_coefficient_of_determination,
    compute_mean_squared_error,
    compute_measure_of_deviation,
)
from schemas.approximation import (
    ApproximationRequest,
    ApproximationResponse,
    ApproximationResultData,
    ApproximationResultSchema,
)


class ApproximationService:
    async def approximate(self, data: ApproximationRequest) -> ApproximationResponse:
        results: List[ApproximationResultSchema] = []
        for MethodClass in approximation_methods:
            method = MethodClass(data.xs, data.ys)

            # Validate approximation method
            validation_result = method.validate()
            if validation_result.success:
                # If method is valid, add successful result
                approximation_result = method.run()
                results.append(
                    ApproximationResultSchema(
                        type_=method.type_,
                        success=True,
                        data=ApproximationResultData(
                            measure_of_deviation=compute_measure_of_deviation(
                                data.xs,
                                data.ys,
                                approximation_result.function,
                            ),
                            mse=compute_mean_squared_error(
                                data.xs,
                                data.ys,
                                approximation_result.function,
                            ),
                            coefficient_of_determination=compute_coefficient_of_determination(
                                data.xs,
                                data.ys,
                                approximation_result.function,
                            ),
                            parameters=approximation_result.parameters,
                        ),
                    )
                )
            else:
                # If method is not valid, add failed result
                results.append(
                    ApproximationResultSchema(
                        type_=method.type_,
                        success=False,
                        message=validation_result.message,
                    )
                )

        return ApproximationResponse(results=results)
