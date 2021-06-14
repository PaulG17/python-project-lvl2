import os
import json
import yaml


def read_file(file_path):
    file_extension = os.path.splitext(file_path)[-1]
    if file_extension in {'.yaml', '.yml'}:
        with open(file_path, 'r', encoding='utf-8') as file_obejct:
            file = yaml.safe_load(file_obejct)
        return file    
    elif file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file_object:
            file = json.load(file_object)
        return file
