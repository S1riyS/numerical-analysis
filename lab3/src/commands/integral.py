from typing import Optional

import click

from commands.args import IntegralArgs
from logger import GlobalLogger
from methods import MethodFactory, MethodType
from methods.rectangle import RectangleMethodMode
from models.discontinuity import DiscontinuityKind
from models.integral import Integral

logger = GlobalLogger()


def __run(args: IntegralArgs) -> None:
    # Create integral
    integral = Integral(args.function, args.left, args.right)
    logger.info(f"Integral: {integral}")

    # Check convergence
    discontinuinties = integral.find_discontinuities()
    found_essential_discontinuity = False
    if discontinuinties:
        logger.warning(f"Discontinuities found")
        for discontinuity in discontinuinties:
            if discontinuity.kind == DiscontinuityKind.ESSENTIAL:
                found_essential_discontinuity = True

            logger.warning(f"\t{discontinuity}")

    if found_essential_discontinuity:
        logger.error("Integral does not converge due to essential discontinuity")
        return

    # Create method
    method_factory = MethodFactory(integral, args.epsilon)
    method_instance = method_factory.get_method(args.method, mode=args.rect_mode)

    logger.info(f"Chosen method: {method_instance}")

    # Evaluate integral
    result = method_instance.solve()

    logger.info(f"Result: {result}")


@click.command()
@click.option("-f", "--function", help='Math function. Example: "x^2 + sin(x - 1)"')
@click.option("-l", "--left", type=float, help="Left border (real number)")
@click.option("-r", "--right", type=float, help="Right border (real number)")
@click.option("-e", "--epsilon", type=float, help="Precision", default=0.01, show_default=True)
@click.option(
    "-m",
    "--method",
    type=click.Choice([m.value for m in MethodType], case_sensitive=False),
    help="Integration method",
)
@click.option(
    "--rect-mode",
    type=click.Choice([rm.value for rm in RectangleMethodMode], case_sensitive=False),
    help="Rectangle method mode (optional)",
    required=False,
)
def integral(
    function: str,
    left: float,
    right: float,
    epsilon: float,
    method: str,
    rect_mode: Optional[str],
) -> None:
    """Evaluate integral with parameters from console"""

    args = IntegralArgs(function, left, right, epsilon, method, rect_mode)

    is_valid, errors = args.validate()
    if not is_valid:
        for error in errors:
            logger.error(error.message)
        return

    __run(args)


@click.command()
@click.argument(
    "json-file",
    type=click.Path(exists=True),
)
def integral_from_json(json_file: str) -> None:
    """Evaluate integral with parameters from JSON file"""

    args = IntegralArgs.from_json(json_file)

    is_valid, errors = args.validate()
    if not is_valid:
        for error in errors:
            logger.error(error.message)
        return

    __run(args)
