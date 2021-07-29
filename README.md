### Hexlet tests and linter status:
[![hexlet-check](https://github.com/PaulG17/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/PaulG17/python-project-lvl2/actions)
[![Python CI](https://github.com/PaulG17/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/PaulG17/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/57f0973750563e5d34bc/maintainability)](https://codeclimate.com/github/PaulG17/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/57f0973750563e5d34bc/test_coverage)](https://codeclimate.com/github/PaulG17/python-project-lvl2/test_coverage)


### Welcome to the [Hexlet Project #2](https://ru.hexlet.io/categories/python/courses)!

GENerator of DIFFerences - detecting the difference between two files YAML/JSON with generating a report containing differences.


### Features:
- [X] Support for different input formats: yaml, json    
- [X]  Create a report (plain text, stylish, json format)    

### Parameters
| arguments| name | comment | 
|:----------------:|:---------|:----------------|
| required| gendiff -h | gendiff [-h] [-f {json,plain,stylish}] first_file second_file |
| positional | first_file | first file to compare |  
| positional | second_file |second file to compare |
| optional | -h, --help | show this help message and exit |
| optional | -f {json,plain,stylish} | set output format (default: 'stylish') |
| optional | --format {json,plain,stylish} | set output format (default: 'stylish') |

## Installation
[Install Git](https://github.com/git-guides/install-git)  
[Install Poetry](https://github.com/python-poetry/poetry)  
git clone git@github.com:PaulG17/python-project-lvl2.git Hexlet-project  
poetry update

## Examples:
### Comparison of flat files (JSON)
```bash
gendiff simple_before.json simple_after.json
```
[![asciicast](https://asciinema.org/a/ZGSj7cidHqLADHGU8lqxje0nK.svg)](https://asciinema.org/a/ZGSj7cidHqLADHGU8lqxje0nK)

### Comparison of flat files (YAML)
```bash
gendiff filepath1.yaml filepath2.yaml
```
[![asciicast](https://asciinema.org/a/2yF5N9lqdHNqYrcV1TbTWu0dV.svg)](https://asciinema.org/a/2yF5N9lqdHNqYrcV1TbTWu0dV)
