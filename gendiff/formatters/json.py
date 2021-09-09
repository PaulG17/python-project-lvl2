import json
from gendiff.formatters.sort_keys import sorted_keys


def format_json(diff):
    return json.dumps({'data': sorted_keys(diff)}, indent=2)
