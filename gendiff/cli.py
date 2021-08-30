import argparse
from gendiff.formatters.format_diff import default_style, formats

def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='first file adress')
    parser.add_argument('second_file', type=str, help='second file adress')
    parser.add_argument('-f', '--format', type=str, help='output format', choices=formats.keys(),
                        default=default_style)
    return parser.parse_args()
