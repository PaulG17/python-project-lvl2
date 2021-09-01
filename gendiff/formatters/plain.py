import gendiff.generate_diff
import gendiff.formatters.sort_keys


COMPLEX = '[complex value]'
ADDED = "Property {0} was added with value: {1}"
REMOVED = "Property {0} was removed"
UPDATED = "Property {0} was updated. From {1} to {2}"


def format_plain(data):
    sorted = sorted_keys(data)
    result = string(sorted)
    return result

def string(tree, prefix=""):
    return '\n'.join(filter(lambda x: x != '', map(lambda x: format_node(x, prefix),tree)))

def format_node(node, prefix=""):
    if node['status'] == nested:
        prefix += f'{node["key"]}.'
        return string(node['value'], prefix)
    return get_line(node, prefix)

def get_line(data, prefix):
    key = f'\'{prefix}{data["key"]}\''

    if data["status"] == ADDED:
        return ADDED.format(key, format(data["value"]))
    elif data["status"] == REMOVED:
        return REMOVED.format(key)
    elif data["status"] == UPDATED:
        return UPDATED.format(key,format(data["value"]["old"]),format(data["value"]["new"]))
    else:
        return ''

def format(data):
    if isinstance(data, list) or isinstance(data, dict):
        return COMPLEX
    elif isinstance(data, str):
        return f'\'{data}\''
    else:
        if data is True:
            return 'true'
        elif data is False:
            return 'false'
        elif data is None:
            return 'null'
        return data
