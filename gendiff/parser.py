import json
import yaml
from pathlib import Path

def get_dict_from_file(path_file):
    file_extension = Path(path_file).suffix
    return open_file(path_file, file_extension)

def parser(file_data, file_type):
    loading = {
        '.json': json.loads,
        '.yaml': lambda file_data:
            yaml.load(file_data, Loader=yaml.SafeLoader)
        }
    return loading[file_type](file_data)

