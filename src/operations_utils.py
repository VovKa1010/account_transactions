from json import load as load_json
from datetime import datetime


def load_operations_json(path: str) -> list:
    """Читает json файл operations.json"""
    with open(path, 'r') as operations_json:
        data_json = load_json(operations_json)
    return data_json


def sort_date_operations(data_operations: list) -> list:
    """Сортировка операций по убыванию даты"""
    return sorted(data_operations, key=sort_date_key, reverse=True)


def sort_date_key(item):
    """Функция ключа для сортировки по дате"""
    if 'date' in item:
        return datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f")
    else:
        return datetime(1, 1, 1)


def executed_operations(data_operations: list):
    """Выбирает все операции со статусом EXECUTED"""
    return [item for item in data_operations if 'state' in item and item["state"] == "EXECUTED"]


def formatting_item_to_account_transaction(item: dict) -> str:
    """Форматирует операцию для вывода"""
    return f"""{get_date_dd_mm_yyyy(item["date"])} {item['description']}
{invoice_formatting(item['from']) if 'from' in item else "нету"} -> {invoice_formatting(item['to'])}
{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"""


def get_date_dd_mm_yyyy(date_str: str) -> str:
    """Приводит строку даты к формату '%d.%m.%Y'"""
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")


def invoice_formatting(invoice: str) -> str:
    """Маскировка номера"""
    items = invoice.strip().split(' ')

    if len(items) < 2:
        return ""

    name = f"{' '.join(items[:-1])}"
    number = items[-1]

    if name == "Счет":
        number = f"**{number[-4:]}"
    else:
        number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return f"{name} {number}"
