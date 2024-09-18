import operations_utils

data_operations = operations_utils.sort_date_operations(
    operations_utils.executed_operations(
        operations_utils.load_operations_json("../operations.json")))

for item in data_operations[0:4]:
    print(operations_utils.formatting_item_to_account_transaction(item), end="\n\n")

