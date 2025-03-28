from commands import cli
from commands.integral import integral, integral_from_json
from logger import GlobalLogger

logger = GlobalLogger()

if __name__ == "__main__":
    try:
        cli.add_command(integral)
        cli.add_command(integral_from_json)
        cli()
    except Exception as e:
        logger.error(e)
