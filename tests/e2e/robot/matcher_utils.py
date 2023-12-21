possible_types = {"INTEGER": int, "FLOAT": float}


def check_type(value: str, expected_type: str) -> bool:
    return isinstance(value, possible_types[expected_type])