from gendiff import generate_diff
import tests.expected as expected
import os


def get_fixture_path(filename):
    result = os.path.abspath(filename)
    return result


def test_string():
    actual = generate_diff(
        get_fixture_path('example1.json'),
        get_fixture_path('example2.json'),
        'string')
    assert actual == expected, 'Файлы не равны'

