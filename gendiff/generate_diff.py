from gendiff.formatters.format_diff import format_diff
from gendiff.open import read_file
from tree import get_key_diff


def generate_diff(file_one_path, file_two_path, format = 'stylish'):
    first_data = read_file(file_one_path)
    second_data = read_file(file_two_path)
    result = get_key_diff(first_data, second_data)
    cat = format_diff(result, format)
    return cat
    