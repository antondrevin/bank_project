import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def converter(currency: str, amount: str) -> Any:
    """Функция принимает валюту и сумму и конвертирует в рубли"""
    to_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={currency}&amount={amount}"

    # payload = {}
    headers = {"apikey": os.getenv("APILAYER_KEY")}

    response = requests.get(url, headers=headers, data={})

    return response.json().get("result")
