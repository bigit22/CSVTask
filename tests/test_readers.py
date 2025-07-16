import pytest
from src.readers import StandardCSVReader

CSV_FILEPATH = 'assets/1.csv'


@pytest.fixture
def reader():
    r = StandardCSVReader(CSV_FILEPATH)
    r.read_csv()
    return r


def test_filter_by_price_less_than_500(reader):
    result = reader.filter_data('price<500')
    assert len(result) == 2
    names = [row['name'] for row in result]
    assert 'redmi note 12' in names
    assert 'poco x5 pro' in names


def test_filter_by_brand_equal_samsung(reader):
    result = reader.filter_data('brand= samsung')
    assert len(result) == 1
    assert result[0]['name'] == 'galaxy s23 ultra'


def test_filter_by_rating_greater_than_4_8(reader):
    result = reader.filter_data('rating>4.8')
    assert len(result) == 1
    assert result[0]['name'] == 'iphone 15 pro'


def test_filter_by_price_equal_199(reader):
    result = reader.filter_data('price=199')
    assert len(result) == 1
    assert result[0]['name'] == 'redmi note 12'


def test_filter_by_price_greater_than_1000(reader):
    result = reader.filter_data('price>1000')
    assert len(result) == 1
    assert result[0]['name'] == 'galaxy s23 ultra'


def test_filter_by_nonexistent_column(reader):
    with pytest.raises(ValueError):
        reader.filter_data('nonexistent=abc')


def test_filter_with_invalid_condition(reader):
    with pytest.raises(ValueError):
        reader.filter_data('invalidcondition')


def test_filter_with_empty_condition(reader):
    result = reader.filter_data('')
    assert result == reader.data


def test_filter_by_price_less_than_equal_500(reader):
    result = reader.filter_data('price<=500')
    assert all(float(row['price']) <= 500 for row in result)


def test_filter_by_rating_less_than_4_8(reader):
    result = reader.filter_data('rating<4.8')
    for row in result:
        assert float(row['rating']) < 4.8
