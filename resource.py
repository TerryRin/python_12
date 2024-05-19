from pathlib import Path


def path(file_name):
    return str(Path(__file__).parent.joinpath(f'tests/resources/{file_name}'))