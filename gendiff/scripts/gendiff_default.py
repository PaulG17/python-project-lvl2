from gendiff.open import read_file
from gendiff.generate_diff import generate_diff
from gendiff.formatters.format_diff import format_diff, default_style


def generate_diff(first_file_path, second_file_path, format=default_style):
    first_file = read_file(first_file_path)
    second_file = read_file(second_file_path)
    diff = generate_diff(first_file, second_file)
    return format_diff(diff, format)

if __name__ == "__main__":
    main()
