from argparse import Namespace

from src.parsers import ArgParser
from src.services import ApplicationService


def main(args: Namespace):
    app = ApplicationService()
    app.open_csv(args.file)

    if args.where:
        app.filter_data(args.where)

    if args.aggregate:
        app.aggregate_data(args.aggregate)

    app.print_result()


if __name__ == '__main__':
    main(ArgParser.parse_args())
