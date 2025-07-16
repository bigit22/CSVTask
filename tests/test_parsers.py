import pytest
from src.parsers import ArgParser


def test_parse_args_with_all_arguments():
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file == 'data.csv'
    assert args.where == 'column>5'
    assert args.aggregate == 'sum'


def test_parse_args_with_partial_arguments():
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file == 'data.csv'
    assert args.where is None
    assert args.aggregate is None


def test_parse_args_with_no_arguments():
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file is None
    assert args.where is None
    assert args.aggregate is None


def test_parse_args_with_only_where():
    parser = ArgParser()
    args = parser.parse_args()
    assert args.where == 'column<10'
    assert args.file is None
    assert args.aggregate is None
