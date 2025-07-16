import pytest
import sys
from src.parsers import ArgParser


def test_parse_args_with_all_arguments(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'program_name',
        '--file', 'assets/1.csv',
        '--where', 'column>5',
        '--aggregate', 'sum'
    ])
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file == 'assets/1.csv'
    assert args.where == 'column>5'
    assert args.aggregate == 'sum'


def test_parse_args_with_partial_arguments(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'program_name',
        '--file', 'data.csv'
    ])
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file == 'data.csv'
    assert args.where is None
    assert args.aggregate is None


def test_parse_args_with_no_arguments(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['program_name'])
    parser = ArgParser()
    args = parser.parse_args()
    assert args.file is None
    assert args.where is None
    assert args.aggregate is None


def test_parse_args_with_only_where(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'program_name',
        '--where', 'column<10'
    ])
    parser = ArgParser()
    args = parser.parse_args()
    assert args.where == 'column<10'
    assert args.file is None
    assert args.aggregate is None
