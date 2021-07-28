import gendiff


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
            data = format_data(node['data before'], formatting)
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

