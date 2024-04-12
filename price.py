import datetime
import csv
from typing import Dict, List

def read_product_data(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        product_data = [
            {'product_name': row[0], 'date': row[1], 'price': float(row[2])}
            for row in reader
        ]
    return product_data

def get_price_changes(product_data: List[Dict[str, str]], product_name: str) -> List[float]:
    one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    prices = [
        item['price']
        for item in product_data
        if item['product_name'] == product_name and 
           datetime.datetime.strptime(item['date'], '%Y-%m-%d') >= one_month_ago
    ]
    return prices
