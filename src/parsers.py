from argparse import Namespace, ArgumentParser


class ArgParser:
    @staticmethod
    def parse_args() -> Namespace:
        parser: ArgumentParser = ArgumentParser()
        parser.add_argument('--file', help='Path to the CSV file')
        parser.add_argument('--where', help='Filter rows by condition')
        parser.add_argument('--aggregate', help='Aggregate rows by condition')
        args: Namespace = parser.parse_args()
        return args
