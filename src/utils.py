import os
import json

from src.products import Product
from src.category import Category


def read_json(way_files):
    path = os.path.abspath(way_files)
    with open(path, 'r', encoding="utf-8") as f:
        categoryes = json.load(f)
        return categoryes


def create_object(data):
    categoryes = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categoryes.append(Category(**category))
    return categoryes
