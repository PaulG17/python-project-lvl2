def format_stylish(tree):
    return get_diff_stylish(tree)


def get_diff_stylish(tree, subst=0):
    result = '{\n'
    formatting = '  '
    for i in range(subst):
        formatting += '    '
    tree.sort(key=lambda x: x['key'])
    for node in tree:
        if node['status'] == 'changed':
            data = format_data(node['value']['old'], formatting)
            result += f"{formatting}- {node['key']}: {data}\n"
            data = format_data(node['value']['new'], formatting)
            result += f"{formatting}+ {node['key']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['value'], formatting)
            result += f"{formatting}+ {node['key']}: {data}\n"
        if node['status'] == 'removed':
            data = format_data(node['value'], formatting)
            result += f"{formatting}- {node['key']}: {data}\n"
        if node['status'] == 'equal':
            data = format_data(node['value'], formatting)
            result += f"{formatting}  {node['key']}: {data}\n"
        if node['status'] == 'nested':
            data = get_diff_stylish(node['value'], subst + 1)
            result += f"{formatting}  {node['key']}: {data}\n"
    result += formatting[:-2] + '}'
    return result


def format_data(three, formatting):
    if type(three) is dict:
        formatting += '    '
        result = '{\n'
        for key in three.keys():
            value = format_data(three[key], formatting)
            result += formatting + '  ' + key + ': ' + value + '\n'
        result += formatting[:-2] + '}'
    elif three is False:
        result = 'false'
    elif three is True:
        result = 'true'
    elif three is None:
        result = 'null'
    else:
        result = str(three)
    return result
