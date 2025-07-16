from argparse import Namespace

from tabulate import tabulate

from src.parsers import ArgParser
from src.readers import StandardCSVReader


def main(args: Namespace):
    reader = StandardCSVReader(args.file)
    reader.read_csv()

    if args.where:
        reader.filter_data(args.where)

    if args.aggregate:
        data = list(reader.aggregate_data(args.aggregate).values())[0]
        output_data = [['min'], [data]]
        print(tabulate(output_data, tablefmt='grid'))

    elif reader.data:
        print(tabulate(reader.data, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main(ArgParser.parse_args())
