from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mutmut import Config, Context


def pre_mutation(context: "Context"):

    filename: str = context.filename
    config: "Config" = context.config

    filename = filename[len("rich/") :] if filename.startswith("rich/") else filename

    # temporary to simplify test time
    if context.mutation_id_of_current_index.index > 25:
        context.skip = True
        return

    test_file = f"test_{filename}"
    if Path(__file__).parent.joinpath("tests", test_file).is_file():
        config.test_command = f"pytest -x tests/{test_file}"
    else:
        context.skip = True
