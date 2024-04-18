import os
import pytest
import json
from save_load_manager import (
    SavaLoadSystem,
)  # Replace 'your_module_name' with the actual module name


@pytest.fixture
def save_load_system(tmpdir):
    return SavaLoadSystem(".json", tmpdir)


def test_save_and_load(save_load_system):
    data = {"key": "value"}
    save_load_system.save(data, "test_file")
    loaded_data = save_load_system.load("test_file")
    assert loaded_data == data


def test_load_default_value(save_load_system):
    default_value = {"default": "value"}
    loaded_data = save_load_system.load(
        "non_existing_file", default_value=default_value
    )
    assert loaded_data == default_value


def test_invalid_json_format(tmpdir):
    # Creating an invalid JSON file
    file_path = os.path.join(tmpdir, "invalid_json.json")
    with open(file_path, "w") as f:
        f.write("invalid JSON")

    sava_load_system = SavaLoadSystem(".json", tmpdir)
    with pytest.raises(json.JSONDecodeError):
        sava_load_system.load("invalid_json")
