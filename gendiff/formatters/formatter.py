from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import format_json


def format_diff(tree, format_name):
    if format_name == 'stylish':
        return stylish(tree)
    elif format_name == 'json':
        return format_json(tree)
    raise 'Format not supported!'