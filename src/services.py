from tabulate import tabulate
from typing import Optional

from src.readers import StandardCSVReader


class ApplicationService:
    def __init__(self):
        self.reader: Optional[StandardCSVReader] = None
        self.aggregated_output: Optional[list] = None

    def open_csv(self, filename: str):
        try:
            self.reader = StandardCSVReader(filename)
            self.reader.read_csv()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            exit(1)
        except TypeError:
            print("Invalid file '{filename}' format.")
            exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(1)

    def filter_data(self, condition: str):
        try:
            self.reader.filter_data(condition)
        except ValueError:
            print(f"Possible invalid condition: '{condition}'")
            exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(1)

    def aggregate_data(self, condition: str):
        try:
            data = (
                list(self.reader.aggregate_data(condition).values())
            )[0]
            self.aggregated_output = [[self.reader.aggregate_operator], [data]]
        except ValueError:
            print(f"Possible invalid condition: '{condition}'")
            exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(1)

    def print_result(self):
        if self.aggregated_output:
            print(tabulate(self.aggregated_output, tablefmt='grid'))
        elif self.reader.data:
            print(tabulate(self.reader.data, headers='keys', tablefmt='psql'))
        else:
            print("No data to print.")
