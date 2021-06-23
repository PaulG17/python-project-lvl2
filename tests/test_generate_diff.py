from gendiff import generate_diff
import pathlib
import pytest

def get_fixture_path(filename):
    test_folder_path = pathlib.Path(__file__).parent.absolute()
    return str(test_folder_path / 'fixtures' / filename)

def get_fixture_data(filename):
    path = get_fixture_path(filename)
    with open(path) as file:
        return file.read()

@pytest.mark.parametrize(("test_input", "expected"), [("", "stylish"), ("json", "json"), ("yaml", "yaml")]) #default/json,yaml/output
def test_actual(test_input, expected):
    actual = generate_diff(
        get_fixture_path(f'example1.{test_input}'),
        get_fixture_path(f'example2.{test_input}'),
     )
    assert actual == get_fixture_data(f'result.{expected}')
