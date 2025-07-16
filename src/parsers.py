from argparse import Namespace, ArgumentParser
from typing import Optional


class ArgParser:
    def __init__(self):
        self.args: Optional[Namespace] = None

    def parse_args(self, args) -> Namespace:
        parser: ArgumentParser = ArgumentParser()
        parser.add_argument('--file', help='Path to the CSV file')
        parser.add_argument('--where', help='Filter rows by condition')
        parser.add_argument('--aggregate', help='Aggregate rows by condition')
        self.args = parser.parse_args(args)
        return self.args
