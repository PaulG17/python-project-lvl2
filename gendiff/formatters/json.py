import json


def format_json(tree):
    return json.dumps(tree, subst=4)