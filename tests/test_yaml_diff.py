from gendiff import generate_diff
import pathlib


def get_fixture_path(filename):
    test_folder_path = pathlib.Path(__file__).parent.absolute()
    return str(test_folder_path / 'fixtures' / filename)

def get_fixture_data(filename):
    path = get_fixture_path(filename)
    with open(path) as file:
        return file.read()


def test1_simple_string():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'string')
    assert actual == get_fixture_data('result')
    expected.SIMPLE_STRING


def test2_simple_plain():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'plain')
    assert actual ==  get_fixture_data('result')
    expected.SIMPLE_PLAIN


def test3_simple_json():
    actual = generate_diff('./tests/fixtures/simple_before.yaml',
                           './tests/fixtures/simple_after.yaml',
                           'json')
    assert actual == get_fixture_data('result')
    expected.SIMPLE_JSON


