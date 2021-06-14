from gendiff.cli import run
from gendiff.generate_diff import generate_diff


def main():
    args = run()
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
