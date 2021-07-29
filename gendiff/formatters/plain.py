def plain(three):
    three.sort(key=lambda x: x['name'])
    result = get_diff_list(three)
    return '\n'.join(result)


def get_diff_list(three, path=''):
    result = []
    for node in three:
        if node['status'] == 'nested':
            change_path = path + node['name'] + '.'
            difference = get_diff_list(node['children'], change_path)
            result.extend(difference)
        if node['status'] == 'added':
            change_path = path + node['name']
            change = change_create(node['data'])
            difference = (
                f"Property '{change_path}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            change_path = path + node['name']
            difference = "Property '{}' was removed".format(change_path)
            result.append(difference)
        if node['status'] == 'changed':
            change_path = path + node['name']
            change_before = change_create(node['data before'])
            change_after = change_create(node['data after'])
            difference = (
                f"Property '{change_path}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result


def change_create(input):
    if type(input) is dict or type(input) is list:
        result = '[complex value]'
    elif input is None:
        result = 'null'
    elif input is False:
        result = 'false'
    elif input is True:
        result = 'true'
    elif type(input) is str:
        result = "'{}'".format(input)
    else:
        result = '{}'.format(input)
    return result

