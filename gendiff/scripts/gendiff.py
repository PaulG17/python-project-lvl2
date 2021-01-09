import argparse
parser = argparse.ArgumentParser(description='hexlet project lvl2')
parser.add_argument("-h","--help", action="store_true",
                                   help="help information",)
answer = "
usage: gendiff [-h] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
"
print(answer)


