possible_types = {"INTEGER": int, "FLOAT": float, "STRING": str}


def check_type(value: str, expected_type: str):
    try:
        # Convert the value to the type
        # If there is no type error then the check type passes
        possible_types[expected_type](value)
    except ValueError:
        raise Exception(f"Type error {value} is not type {expected_type}")


def list_contains(input_list: list, contains_str: str):
    for item in input_list:
        if contains_str in str(item):
            return
    raise Exception(f"List {input_list} does not contain {contains_str}")
