import datetime
import csv
import os
from dateutil.relativedelta import relativedelta
import pytest
from price import read_data, analyze_price_changes

@pytest.fixture
def sample_data():
    return [
        (datetime.date(2024, 3, 15), 2.50),
        (datetime.date(2024, 3, 20), 2.60),
        (datetime.date(2024, 3, 25), 2.70)
    ]

@pytest.fixture
def data_file(tmpdir, sample_data):
    filename = tmpdir.join("data.txt")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for date, price in sample_data:
            writer.writerow(['Milk', date.strftime('%Y-%m-%d'), price])
    return filename

def test_read_data(data_file, sample_data):
    assert read_data(data_file, 'Milk') == sample_data

def test_analyze_price_changes(sample_data):
    result = analyze_price_changes(sample_data)
    assert result == "Зміна ціни: 0.20. Початкова ціна: 2.50, Кінцева ціна: 2.70"
