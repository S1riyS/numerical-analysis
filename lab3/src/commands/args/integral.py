import json
from dis import disco
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from logger import GlobalLogger
from methods import MethodFactory, MethodType
from methods.rectangle import RectangleMethodMode
from models.discontinuity import DiscontinuityKind
from models.integral import Integral
from models.response import ErrorResponse

logger = GlobalLogger()

E = TypeVar("E", bound=Enum)


class IntegralArgs:
    def __init__(
        self,
        function: str,
        left: float,
        right: float,
        epsilon: float,
        method: str,
        rect_mode: Optional[str] = None,
    ) -> None:
        self.function = function
        self.left = left
        self.right = right
        self.epsilon = epsilon
        self.method = self.__parse_to_enum(method, MethodType)

        # Set rectangle method mode if rectangle method is chosen
        self.rect_mode: Optional[RectangleMethodMode] = None
        if self.method == MethodType.RECTANGLE and rect_mode is not None:
            self.rect_mode = self.__parse_to_enum(rect_mode, RectangleMethodMode)

    @classmethod
    def from_json(cls, file_path: str) -> "IntegralArgs":
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            return cls.__create_from_dict(data)

        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except PermissionError:
            raise ValueError(f"Permission denied: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file: {file_path}") from e

    @classmethod
    def __create_from_dict(cls, data: Dict[str, Any]) -> "IntegralArgs":
        """Validate and create instance from dictionary"""
        # Check required fields
        required_fields = ["function", "left", "right", "epsilon", "method"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")

        # Return instance
        return cls(
            function=data["function"],
            left=data["left"],
            right=data["right"],
            epsilon=data["epsilon"],
            method=data["method"],
            rect_mode=data.get("rect-mode"),
        )

    @staticmethod
    def __parse_to_enum(value: str, EnumClass: Type[E]) -> E:
        """
        Parse string to enum.

        Args:
            value (str): String to be parsed.
            EnumClass (Type[E]): Enum class to which the value should be parsed.

        Returns:
            E: Parsed enum value.

        Raises:
            ValueError: If parsed value is not valid for the given enum class.
        """
        try:
            return EnumClass(value)
        except ValueError:
            raise ValueError(f"Invalid {EnumClass.__name__} value: {value}")

    def validate(self) -> Tuple[bool, List[ErrorResponse]]:
        validation_errors: List[ErrorResponse] = []
        if self.left >= self.right:
            validation_errors.append(ErrorResponse("bounds", "Left border must be less than right border"))

        if self.epsilon <= 0:
            validation_errors.append(ErrorResponse("precision", "Precision must be greater than 0"))
        elif self.epsilon > 1:
            logger.warning("Usually precision is set to value less than 1")

        if validation_errors:
            return False, validation_errors
        return True, []
