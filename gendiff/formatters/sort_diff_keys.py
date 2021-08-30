sort_diff_keysfrom gendiff.get_tree_diff import nested


def sort_keys(data):
    data = sorted(data, key=lambda x: x['key'])
    for item in data:
        if item["status"] == nested:
            item["value"] = sort_keys(item["value"])
    return data
