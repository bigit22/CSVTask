from argparse import Namespace

from tabulate import tabulate

from src.parsers import ArgParser
from src.readers import StandardCSVReader


def main(args: Namespace):
    reader = StandardCSVReader('assets/1.csv')
    reader.read_csv()

    if args.where:
        reader.filter_data(args.where)

    if args.aggregate:
        pass

    if reader.data:
        print(tabulate(reader.data, tablefmt='grid'))


if __name__ == '__main__':
    main(ArgParser.parse_args())
