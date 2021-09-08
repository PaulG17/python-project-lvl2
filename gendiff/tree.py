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
                'value': first_keys[key],
                'status': 'removed',
            })
        elif key in added_keys:
            diff.append({
                'key': key,
                'value': second_keys[key],
                'status': 'added',
            })
        elif first_keys[key] == second_keys[key]:
            diff.append({
                'key': key,
                'value': first_keys[key],
                'status': 'equal',
            })
        elif isinstance(first_keys[key], dict) and isinstance(second_keys[key], dict):
            diff.append({
                'key': key,
                'value': generate_diff(first_keys[key], second_keys[key]),
                'status': 'nested',
            })
        else:
            diff.append({
                'key': key,
                'value': {
                    'old': first_keys[key],
                    'new': second_keys[key],
                },
                'status': 'changed',
            })
    return diff
