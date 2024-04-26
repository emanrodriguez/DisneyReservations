"""
Util functions that can be used by both client and server

"""
from typing import List, Dict, Optional, Any

def get_enum_value(enum):
    return str(enum).split('.')[-1]

def transform_dict_list(dict_list: Dict, key: str):
    """
    This function transforms a list of dictionaries into a new dictionary.
    In the new dictionary, a specific key’s value from the original 
    dictionaries becomes the new key, and the corresponding value is 
    the remainder of the original dictionary.

    # Input:
    dict_list = [
        {'key': 'A', 'value': 1}, 
        {'key': 'B', 'value': 2}
        ]

    # Output:
    transformed_dict = {
        'A': {'value': 1}, 
        'B': {'value': 2}}
    """
    new_dict = {}
    for d in dict_list:
        if key in d:
            new_key = d.pop(key)
            new_dict[new_key] = d
    return new_dict

    