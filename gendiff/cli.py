import argparse


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='first file adress')
    parser.add_argument('second_file', type=str, help='second file adress')
    parser.add_argument('-f', '--format', type=str, help='output format')
    return parser.parse_args()
