import json
from pathlib import Path

RESOURCES_PATH = Path(__file__).parent.parent.joinpath("resources")


def inject_json_from_file(file):
    file = str(RESOURCES_PATH.joinpath(file))
    with open(file) as f:
        raw_data = json.load(f)
    return raw_data