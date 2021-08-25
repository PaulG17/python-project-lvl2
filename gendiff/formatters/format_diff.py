from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def format_diff(tree, format_name):
    if format_name == 'stylish':
        return stylish(tree)
    elif format_name == 'plain':
        return plain(tree)
    elif format_name == 'json':
        return json(tree)
    raise 'Format not supported!'
