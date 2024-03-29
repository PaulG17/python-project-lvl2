import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',  help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == "__main__":
    main()
