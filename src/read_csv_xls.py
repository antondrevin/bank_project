import csv

import pandas as pd


def read_csv(path: str) -> list[dict]:
    """функция чтения из .csv файла"""
    reader_scv_list = []
    with open(path, encoding="utf-8") as file:
        reader_csv = csv.DictReader(file, delimiter=";")

        for row in reader_csv:
            reader_scv_list.append(row)

    return reader_scv_list


def read_xls(path: str) -> list[dict]:
    """функция чтения из excel файла"""
    df = pd.read_excel(path)
    result = df.to_dict(orient='records')
    return result
