import pytest
import src.operations_utils as operations_utils
from datetime import datetime


@pytest.fixture()
def test_operations():
    return [
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 97584898735659638967"
        },
        {
            "id": 649467725,
            "state": "CANCELED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 3530191547567121",
            "to": "Счет 97584898735659638967"
        },
        {},
        {
            "id": 879660146,
            "state": "EXECUTED",
            "date": "2018-07-22T07:42:32.953324",
            "operationAmount": {
              "amount": "92130.50",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Счет 19628854383215954147",
            "to": "Visa Platinum 3530191547567121"
        },
        {
            "id": 86608620,
            "state": "EXECUTED",
            "date": "2019-08-16T04:23:41.621065",
            "operationAmount": {
              "amount": "6004.00",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Перевод с карты на счет",
            "to": "Visa Platinum 3530191547567121"
        },
        {}]


def test_load_operations_json():
    assert operations_utils.load_operations_json('operations.json')


def test_sort_date_operations(test_operations):
    assert operations_utils.sort_date_operations(test_operations)


def test_executed_operations(test_operations):
    assert len(operations_utils.executed_operations(test_operations)) == 3


def test_formatting_item_to_account_transaction(test_operations):
    assert operations_utils.formatting_item_to_account_transaction(test_operations[0])
    assert operations_utils.formatting_item_to_account_transaction(test_operations[-2])
    with pytest.raises(KeyError):
        operations_utils.formatting_item_to_account_transaction(test_operations[-1])


def test_get_date_dd_mm_yyyy():
    assert operations_utils.get_date_dd_mm_yyyy("2018-06-08T16:14:59.936274") == "08.06.2018"
    with pytest.raises(ValueError):
        assert operations_utils.get_date_dd_mm_yyyy("2018-06-08T16:14:59") == "08.06.2018"


def test_sort_date_key(test_operations):
    assert operations_utils.sort_date_key(test_operations[0]) == datetime(2018, 4, 14, 19, 35, 28, 978265)
    assert operations_utils.sort_date_key(test_operations[-1]) == datetime(1, 1, 1)


def test_invoice_formatting():
    assert operations_utils.invoice_formatting("") == ""
    assert operations_utils.invoice_formatting("Maestro 7552745726849311") == "Maestro 7552 74** **** 9311"
    assert operations_utils.invoice_formatting("Visa Platinum 6942697754917688") == "Visa Platinum 6942 69** **** 7688"
    assert operations_utils.invoice_formatting("Счет 34799481846914116850") == "Счет **6850"
