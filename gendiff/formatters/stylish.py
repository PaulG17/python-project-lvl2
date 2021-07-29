def stylish(tree):
    return get_diff_stylish(tree)


def get_diff_stylish(tree, subst=0):
    result = '{\n'
    formatting = '  '
    for i in range(subst):
        formatting += '    '
    tree.sort(key=lambda x: x['name'])
    for node in tree:
        if node['status'] == 'changed':
            data = get_diff_stylish(node['data before'], formatting)
            result += f"{formatting}- {node['name']}: {data}\n"
            data = format_data(node['data after'], formatting)
            result += f"{formatting}+ {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['data'], formatting)
            result += f"{formatting}+ {node['name']}: {data}\n"
        if node['status'] == 'deleted':
            data = format_data(node['data'], formatting)
            result += f"{formatting}- {node['name']}: {data}\n"
        if node['status'] == 'not changed':
            data = format_data(node['data'], formatting)
            result += f"{formatting}  {node['name']}: {data}\n"
        if node['status'] == 'nested':
            data = get_diff_stylish(node['children'], subst + 1)
            result += f"{formatting}  {node['name']}: {data}\n"
    result += formatting[:-2] + '}'
    return result


def format_data(input, formatting):
    if type(input) is dict:
        formatting += '    '
        result = '{\n'
        for key in input.keys():
            value = format_data(input[key], formatting)
            result += formatting + '  ' + key + ': ' + value + '\n'
        result += formatting[:-2] + '}'
    elif input is False:
        result = 'false'
    elif input is True:
        result = 'true'
    elif input is None:
        result = 'null'
    else:
        result = str(input)
    return result

