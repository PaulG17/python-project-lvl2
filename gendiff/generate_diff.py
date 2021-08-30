from gendiff.open import read_file
from operator import itemgetter


def generate_diff(file_one_path, file_two_path):
    first_data = read_file(file_one_path)
    second_data = read_file(file_two_path)
    first_dict = first_data.keys()
    second_dict = second_data.keys()
    result = []
    deleted_keys = first_dict - second_dict
    added_keys = second_dict - first_dict
    all_keys = second_dict | first_dict
    diff = []
    for key in all_keys:
        if key in deleted_keys:
            diff.append({
                'key': key,
                'value': first_dict[key],
                'status': 'removed',
            })
        elif key in added_keys:
            diff.append({
                'key': key,
                'value': second_dict[key],
                'status': 'added',
            })
        elif first_dict[key] == second_dict[key]:
            diff.append({
                'key': key,
                'value': first_dict[key],
                'status': 'equal',
            })
        elif isinstance(first_dict[key], dict) and isinstance(second_dict[key], dict):
            diff.append({
                'key': key,
                'value': generate_diff(first_dict[key], second_dict[key]),
                'status': 'nested',
            })
        else:
            diff.append({
                'key': key,
                'value': {
                    'old': first_dict[key],
                    'new': second_dict[key],
                },
                'status': 'changed',
            })
    sequence = sorted(result, key=itemgetter(1))
    result = []
    for item in sequence:
        result.append(f"{item[0]} {item[1]}: {item[2]}")
    result_string = f'{{\n{result}\n}}'

    return result_string
    