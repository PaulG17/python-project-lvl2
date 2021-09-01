import gendiff.formatters.stylish 
import gendiff.formatters.plain
import gendiff.formatters.json 


default_style = 'stylish'
formats = {
    'json': format_json,
    'plain': format_plain,
    'stylish': format_stylish,
}

def format_diff(tree, style = default_style):
    if style in formats:
        formatter = formats.get(style)
    else:
        raise RuntimeError(f'{style} not supported!')
    return formatter(tree)    
