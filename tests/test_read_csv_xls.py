from unittest.mock import mock_open, patch

from src.read_csv_xls import read_csv, read_xls


def test_read_csv():
    with patch("builtins.open", mock_open(read_data='id;state\n650703;EXECUTED')):
        assert read_csv("") == [{'id': '650703', 'state': 'EXECUTED'}]


@patch('pandas.read_excel')
def test_read_xls(mock_get):
    mock_get.return_value.to_dict.return_value = [{'id': '650703', 'state': 'EXECUTED'}]
    assert read_xls("") == [{'id': '650703', 'state': 'EXECUTED'}]
