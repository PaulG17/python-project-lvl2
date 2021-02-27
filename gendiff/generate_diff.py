import json
from operator import itemgetter


def generate_diff(file_one_path, file_two_path):
    first_data = json.load(open(file_one_path))
    second_data = json.load(open(file_two_path))
    first_dict_keys = first_data.keys()
    second_dict_keys = second_data.keys()
    result = []
    for k in second_dict_keys - first_dict_keys:  # добавлен
        result.append(('+', k, second_data[k]))
    for k in first_dict_keys - second_dict_keys:  # удален
        result.append(('-', k, first_data[k]))
    for k in first_dict_keys & second_dict_keys:
        if first_data[k] == second_data[k]:
            result.append((' ', k, first_data[k]))  # равен
        if first_data[k] != second_data[k]:
            result.append(('-', k, first_data[k]))  # не равен
            result.append(('+', k, second_data[k]))  # не равен
    sequence = sorted(result, key=itemgetter(1))
    result = []
    for item in sequence:
        result.append(f"{item[0]} {item[1]}: {item[2]}")
    result_string = f'{{\n{result}\n}}'

    print(result_string)
