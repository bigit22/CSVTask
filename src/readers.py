import re
from csv import DictReader
from typing import Optional

from src.entities import Row, FILTER_OPERATORS


class StandardCSVReader:
    def __init__(self, filepath: str, /):
        self.filepath: str = filepath
        self.data: Optional[list] = None

    def read_csv(self) -> None:
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            reader: DictReader = DictReader(f)
            data = list(reader)
        self.data = data

    def filter_data(self, condition) -> list[Row]:
        column, op, value_str = self._parse_condition(condition)
        self._validate_column(column)
        filter_value = self._cast_value(value_str)
        print(self.data)
        return [row for row in self.data if self._row_matches(row, column, op, filter_value)]

    def aggregate_data(self, condition: str) -> dict[str, float | Optional[str]]:
        column, operation = self._parse_aggregate_condition(condition)
        self._validate_column(column)
        values: list[float] = self._extract_numeric_values(column)

        if not values:
            return {column: None}

        result = self._compute_aggregation(values, operation)
        return {column: result}

    @staticmethod
    def _compute_aggregation(values: list[float], operation: str) -> float:
        if operation == 'avg':
            return sum(values) / len(values)
        elif operation == 'min':
            return min(values)
        elif operation == 'max':
            return max(values)
        else:
            raise ValueError(f'Unknown aggregation operation: {operation}')

    def _extract_numeric_values(self, column: str) -> list[float]:
        values = []
        for row in self.data:
            val_str = row[column]
            if self._is_number(val_str):
                values.append(float(val_str))
            else:
                raise ValueError(f'Column "{column}" contains non-numeric data')
        return values

    @staticmethod
    def _is_number(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def _parse_aggregate_condition(condition: str) -> tuple:
        pattern: str = r'^\s*(\w+)\s*=\s*(avg|min|max)\s*$'
        match: re.Match = re.match(pattern, condition)
        if not match:
            raise ValueError(f'Invalid aggregate condition: {condition}')
        col, op = match.groups()
        return col, op

    @staticmethod
    def _parse_condition(condition: str) -> tuple:
        pattern = r'^\s*(\w+)\s*([<>=])\s*(.+)\s*$'
        match = re.match(pattern, condition)
        if not match:
            raise ValueError(f'Invalid filter condition: {condition}')
        column, op, value_str = match.groups()
        return column, op, value_str

    def _validate_column(self, column: str):
        if not self.data:
            return
        if column not in self.data[0]:
            raise ValueError(f'column {column} does not exist')

    @staticmethod
    def _cast_value(val: str) -> float | str:
        try:
            return float(val)
        except ValueError:
            return val

    def _row_matches(self, row: Row, column: str, op: str, filter_value: float| str) -> bool:
        cell = row[column]
        cell_value = self._cast_value(cell)
        if isinstance(filter_value, float) and isinstance(cell_value, float):
            return FILTER_OPERATORS[op](cell_value, filter_value)
        else:
            if op != '=':
                return False
            return cell == str(filter_value)
