from typing import Any

def function_receives_value(value: Any) -> tuple:
    value_list = sorted(value)
    value_list_tuple = list(value_list)
    value_list_tuple_tuple = tuple(value_list_tuple)
    return value_list_tuple_tuple


