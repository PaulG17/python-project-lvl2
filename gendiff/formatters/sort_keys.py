def sorted_keys(tree):
    data = sorted(tree, key=lambda x: x['key'])
    for item in data:
        if item["status"] == 'nested':
            item["value"] = sorted_keys(item["value"])
    return data
