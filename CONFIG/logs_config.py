import pathlib

GREY = "\x1b[1;37m"
BLUE = "\x1b[1;34m"
YELLOW = "\x1b[33;20m"
RED = "\x1b[31;20m"
BOLD_RED = "\x1b[41m"
RESET = "\x1b[0m"
LOGGER_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] -> %(message)s"

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
LOGS_PATH = PROJECT_ROOT / "LOGS"
