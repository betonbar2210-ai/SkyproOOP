import json
import os

from unittest.mock import patch, mock_open

from src.utils import read_json, create_object


def test_read_json_try(utils_json):
    way_file = os.path.abspath("../data/products.json")
    mock_json = mock_open(read_data=json.dumps(utils_json))
    with patch("builtins.open", mock_json):
        assert read_json(way_file) == utils_json

