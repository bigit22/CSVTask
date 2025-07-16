Row = dict[str, str]

FILTER_OPERATORS = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b,
}
