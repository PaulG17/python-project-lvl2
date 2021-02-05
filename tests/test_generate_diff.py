from gendiff.generator import generate_diff
import tests.expected as expected


def test_string():
    actual = generate_diff('./tests/fixtures/example1.json',
                           './tests/fixtures/example2.json',
                           'string')
    assert actual == expected.SIMPLE_STRING, 'Файлы не равны'
