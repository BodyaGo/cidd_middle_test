import pytest
from script import read_product_data, get_price_changes

@pytest.fixture
def sample_product_data():
    return [
        {'product_name': 'Widget', 'date': '2024-03-15', 'price': 10.0},
        {'product_name': 'Widget', 'date': '2024-03-20', 'price': 12.0},
        {'product_name': 'Widget', 'date': '2024-03-25', 'price': 15.0},
        {'product_name': 'Gadget', 'date': '2024-03-15', 'price': 20.0},
        {'product_name': 'Gadget', 'date': '2024-03-20', 'price': 22.0},
        {'product_name': 'Gadget', 'date': '2024-03-25', 'price': 25.0},
    ]

def test_read_product_data(sample_product_data, tmp_path):
    file_path = tmp_path / "products.txt"
    with open(file_path, 'w') as file:
        file.write("Widget,2024-03-15,10.0\n")
        file.write("Widget,2024-03-20,12.0\n")
        file.write("Widget,2024-03-25,15.0\n")
        file.write("Gadget,2024-03-15,20.0\n")
        file.write("Gadget,2024-03-20,22.0\n")
        file.write("Gadget,2024-03-25,25.0\n")

    assert read_product_data(file_path) == sample_product_data

def test_get_price_changes(sample_product_data):
    assert get_price_changes(sample_product_data, 'Widget') == [12.0, 15.0]
    assert get_price_changes(sample_product_data, 'Gadget') == [22.0, 25.0]
