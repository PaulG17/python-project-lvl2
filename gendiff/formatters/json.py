import json
import gendiff.formatters.sort_keys


def format_json(diff):
    return json.dumps({'data': sort_keys(diff)}, indent=2)
