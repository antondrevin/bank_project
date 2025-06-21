# виджет банковских операций по карте/счету

## Данный виджет предназначен для банковских операций клиента: 
1. Маскировка номера карты клиента;
2. Маскировка номера счета клиента; 
3. Умеет принимать на вход строку с датой в одном и 
возвращает строку с датой в формате "ДД.ММ.ГГГГ"

# Установка

Клонируйте репозиторий:

``` git clone https://github.com/antondrevin/bank_project.git ```

**Установите зависимости, используя менеджер пакетов `poetry`:**
    
``` poetry install```

## Использование

Виджет предоставляет следующие основные функции:

 1. `get_mask_card_number(card_number)`   
Функция возвращает скрытый номер карты в формате:  
`1234 56** **** 7890`  
 2. `get_mask_account(account_number)`  
Функция возвращает скрытый номер счета в формате:  
`**1234`  
 3. `mask_account_card(name_card)`  
Функция определяет формат данных счет/карта, далее с помощью соответствующих   
функций `1` и `2` скрывает номер. Возвращает в формате:  
`ИМЯ КАРТЫ 1234 56** **** 7890`  
или  
`счет ** 7890`  
 4. `get_date(time_card)`  
Функция возвращает строку с датой в формате:  
`ДД.ММ.ГГГГ`  
 5. `filter_by_state(list_state, key_state = "EXECUTED")`  
Функция фильтрует словари по заданному значению для ключа `state`  
 6. `sort_by_date(list_state, sorting = True)`  
Функция возвращает по умолчанию отсортированный по убыванию список по дате
 7. `filter_by_currency(transactions_list, currency)`
Функция возвращает итератор, который поочередно выдает транзакции с соответствующей валютой.
 8. `transaction_descriptions(transactions_list)`
Функция возвращает описание каждой операции по очереди
 9. `card_number_generator(start, end)` 
Функция возвращает номера банковских карт в формате:   
`XXXX XXXX XXXX XXXX`
где X — цифра номера карты
 10. def log(filename)
декоратор для логирования с настройками
 11. def write_log(message, filename)
Функция записывает результат выполнения функции foo в файл

## Примеры использования функций

Python

    state_opration = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    




    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_data("2024-03-11T02:26:18.671407"))
    print(filter_by_state(state_opration))
    print(filter_by_state(state_opration, key_state = "CANCELED"))
    print(sort_by_date(state_opration))
    print(sort_by_date(state_opration, sorting = False))
    gen_usd = filter_by_currency(transactions, "USD")
    gen_rub = filter_by_currency(transactions, "RUB")
    gen_descript = transaction_descriptions(transactions)

    for _ in range(2):
        print(next(gen_usd))

    for _ in range(2):
        print(next(gen_rub))

    for _ in range(4):
        print(next(gen_descript))

    for card_number in card_number_generator(77777, 77779):
        print(card_number)

вывод

    1234 56** **** 3456
    **4305
    счет **9589
    Visa Gold  5999 41** **** 6353
    11.03.2024
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
    {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    0000 0000 0007 7777
    0000 0000 0007 7778
    0000 0000 0007 7779

## Тесты

Структура тестов:

```
tests/
├── test_masks.py # Тесты масок (9 параметризованных тестов)
├── test_processing.py # Тесты обработки (5 фикстур)
├── test_widget.py # Тесты виджетов (6 параметризованных тестов)
└── test_generators.py # Тесты виджетов (12 тестов, 1 фикстура)

```
Покрытие тестами 100%


### Документация

Более подробную документацию по каждой функции можно найти в `docstrings` внутри исходного кода.

### Лицензия

Сведения о лицензии проекта (например, MIT, Apache 2.0) [укажите здесь](https://github.com).

