import json
from pathlib import Path


def read_fixtures(file_name):
    """
    Reads json file from fixtures folder and returns a dictionary
    """

    file_path = Path(__file__).resolve().parent.parent / "fixtures" / file_name
    with open(file_path, "r") as json_file:
        return json.load(json_file)
