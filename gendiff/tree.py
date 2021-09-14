def get_key_diff(first_data, second_data):
    first_keys = first_data.keys()
    second_keys = second_data.keys()
    deleted_keys = first_keys - second_keys
    added_keys = second_keys - first_keys
    all_keys = second_keys | first_keys
    diff = []
    for key in all_keys:
        if key in deleted_keys:
            diff.append({
                'key': key,
                'value': first_data[key],
                'status': 'removed',
            })
        elif key in added_keys:
            diff.append({
                'key': key,
                'value': second_data[key],
                'status': 'added',
            })
        elif first_data[key] == second_data[key]:
            diff.append({
                'key': key,
                'value': first_data[key],
                'status': 'equal',
            })
        elif isinstance(first_data[key], dict) and isinstance(
                second_data[key], dict):
            diff.append({
                'key': key,
                'value': get_key_diff(first_data[key], second_data[key]),
                'status': 'nested',
            })
        else:
            diff.append({
                'key': key,
                'value': {
                    'old': first_data[key],
                    'new': second_data[key],
                },
                'status': 'changed',
            })
    return diff
