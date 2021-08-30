import gendiff.formatters.stylish
import gendiff.formatters.plain
from gendiff.formatters.json import json


formats = {
    'stylish': format_stylish,
    'json': format_json,
    'plain': format_plain
}

default_style = 'stylish'

def format_diff(tree, style = default_style):
    if style in formats:
        formatter = formats.get(style)
    else:
        raise RuntimeError(f'{style} not supported!')
    return formatter(tree)    
