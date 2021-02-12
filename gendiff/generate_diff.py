import json


def main():
    first_data = json.load(open('example1.json'))
    second_data = json.load(open('example2.json'))
    first_dict_keys = first_data.keys()
    second_dict_keys = second_data.keys()
    result = []
    for k in second_dict_keys - first_dict_keys:  # добавлен
        result.append(f"+ {k}: {second_data[k]}")
    for k in first_dict_keys - second_dict_keys:  # удален
        result.append(f"- {k}: {first_data[k]}")
    for k in first_dict_keys & second_dict_keys:
        if first_data[k] == second_data[k]:
            result.append(f"  {k}: {first_data[k]}")  # равен
        if first_data[k] != second_data[k]:
            result.append(f"- {k}: {first_data[k]}")  # не равен
            result.append(f"+ {k}: {second_data[k]}")  # не равен
    final = sorted(result)
    print("\n".join(final))
