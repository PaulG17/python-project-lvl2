from gendiff.generate_diff import generate_diff
import pathlib
import pytest

def get_fixture_path(filename):
    test_folder_path = pathlib.Path(__file__).parent.absolute()
    return str(test_folder_path / 'fixtures' / filename)

def get_fixture_data(filename):
    path = get_fixture_path(filename)
    with open(path) as file:
        return file.read()

@pytest.mark.parametrize(
    "file1,file2,correct_answer,format_name",
    [
        ('file1.json', 'file2.json', 'correct.stylish', 'stylish'),
        ('file1.yaml', 'file2.yaml', 'correct.stylish', 'stylish'),
        ('file1.json', 'file2.json', 'correct.plain', 'plain'),
        ('file1.yaml', 'file2.yaml', 'correct.plain', 'plain'),
        ('file1.json', 'file2.json', 'correct_answer.json', 'json'),
        ('file1.yaml', 'file2.yaml', 'correct_answer.json', 'json')
    ]
)

def test_diff_stylish_json(file1, file2, correct_answer, format_name):
    path_one = get_fixture_path(file1)
    path_two = get_fixture_path(file2)
    path_correct_answer = get_fixture_path(correct_answer)
    with open('{}'.format(path_correct_answer)) as file:
        correct_answer = file.read()
    assert generate_diff(path_one, path_two) == correct_answer
    if format_name == 'stylish':
        assert generate_diff(path_one, path_two) == correct_answer    
    