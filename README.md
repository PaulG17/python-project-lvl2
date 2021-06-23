### Hexlet tests and linter status:
[![Actions Status](https://github.com/PaulG17/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/PaulG17/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/57f0973750563e5d34bc/maintainability)](https://codeclimate.com/github/PaulG17/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/57f0973750563e5d34bc/test_coverage)](https://codeclimate.com/github/PaulG17/python-project-lvl2/test_coverage)


###Welcome to the [Hexlet Project #2](https://ru.hexlet.io/categories/python/courses)!

GENerator of DIFFerences - detecting the difference between two files YAML/JSON with generating a report containing differences.


###Features:
- [X] Support for different input formats: yaml, json    
- [X]  Create a report (plain text, stylish, json format)    

###Parameters
| arguments| name | comment | 
|:----------------:|:---------:|:----------------:|
| required| gendiff -h | gendiff [-h] [-f {json,plain,stylish}] first_file second_file |
| positional | first_file | first file to compare |  
| positional | second_file |second file to compare |
| optional | -h, --help | show this help message and exit |
| optional | -f {json,plain,stylish} | set output format (default: 'stylish') |
| optional | --format {json,plain,stylish} | set output format (default: 'stylish') |

###Example:
```bash
input    
$ gendiff --format plain filepath1.json filepath2.yml
```
```bash
output        
Setting "common.setting1" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group3" was removed
```


