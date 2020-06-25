import os
from utils.misc import clear_text
from utils.validations import is_empty


def string_input(text: str, empty: bool = False, clear: bool = True) -> str:
    """
    Gets an string input from the user

    :param text: the text for the user
    :param empty: (optional) if the string could be empty
    :param clear: (optional) if the extra whitespaces can be removed
    :return: the user´s input string
    """
    if empty:
        return clear_text(input(text)) if clear else input(text)
    else:
        while True:
            value = clear_text(input(text)) if clear else input(text)
            if not is_empty(value):
                return value


def int_input(text: str, min_value: int = None, max_value: int = None, leave_value: int = None) -> int:
    """
    Gets an integer input from the user

    :param text: the text for the user
    :param min_value: (optional) the min accepted value
    :param max_value: (optional) the max accepted value
    :param leave_value: (optional) value to leave (in case of a menu)
    :return: the integer entered by the user
    """
    # Switches the max and min if they are switched
    if max_value is not None and min_value is not None:
        if max_value < min_value:
            max_value, min_value = min_value, max_value

    while True:
        try:
            value = int(clear_text(input(text)))
        except ValueError:
            print('Please enter a valid integer!\n')
        else:
            if leave_value is not None and value == leave_value:
                return value  # Condition -> leave: ok
            if min_value is None:
                if max_value is None:
                    return value  # Condition -> max: ?, min: ?
                else:
                    if max_value >= value:
                        return value  # Condition -> max: ok, min: ?
                    else:
                        # Condition -> max: ok, min: ?
                        if leave_value is not None:
                            print(f'Please, enter a smaller value! (max: {max_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a smaller value! (max: {max_value})\n')
            else:
                if max_value is None:
                    if value >= min_value:
                        return value  # Condition -> max: ?, min: ok
                    else:
                        # Condition -> max: ?, min: ok
                        if leave_value is not None:
                            print(f'Please, enter a higher value! (min: {min_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a higher value! (min: {min_value})\n')
                else:
                    if max_value >= value >= min_value:
                        return value  # Condition -> max: ok, min: ok
                    else:
                        # Condition -> max: ok, min: ok
                        if leave_value is not None:
                            print(f'Please, enter a valid value! '
                                  f'(min: {min_value}, max: {max_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a valid value! (min: {min_value}, max: {max_value})\n')


def float_input(text: str, min_value: float = None, max_value: float = None, leave_value: float = None) -> float:
    """
    Gets an float input from the user

    :param text: the text for the user
    :param min_value: (optional) the min accepted value
    :param max_value: (optional) the max accepted value
    :param leave_value: (optional) value to leave (in case of a menu)
    :return: the float entered by the user
    """
    # Switches the max and min if they are switched
    if max_value is not None and min_value is not None:
        if max_value < min_value:
            max_value, min_value = min_value, max_value

    while True:
        try:
            value = float(clear_text(input(text)))
        except ValueError:
            print('Please enter a valid integer!\n')
        else:
            if leave_value is not None and value == leave_value:
                return value  # Condition -> leave: ok
            if min_value is None:
                if max_value is None:
                    return value  # Condition -> max: ?, min: ?
                else:
                    if max_value >= value:
                        return value  # Condition -> max: ok, min: ?
                    else:
                        # Condition -> max: ok, min: ?
                        if leave_value is not None:
                            print(f'Please, enter a smaller value! (max: {max_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a smaller value! (max: {max_value})\n')
            else:
                if max_value is None:
                    if value >= min_value:
                        return value  # Condition -> max: ?, min: ok
                    else:
                        # Condition -> max: ?, min: ok
                        if leave_value is not None:
                            print(f'Please, enter a higher value! (min: {min_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a higher value! (min: {min_value})\n')
                else:
                    if max_value >= value >= min_value:
                        return value  # Condition -> max: ok, min: ok
                    else:
                        # Condition -> max: ok, min: ok
                        if leave_value is not None:
                            print(f'Please, enter a valid value! '
                                  f'(min: {min_value}, max: {max_value}, leave: {leave_value})\n')
                        else:
                            print(f'Please, enter a valid value! (min: {min_value}, max: {max_value})\n')


def list_input(text: str, sep: str = ',', empty: bool = False, clear: bool = True, list_type: type = str,
               error_message: str = 'Invalid value type!', repeat: bool = True) -> list:
    """
    Gets a list from the user

    :param text: the text for the user
    :param sep: (optional) the list separator
    :param empty: (optional) if the string could be empty
    :param clear: (optional) if the extra whitespaces can be removed
    :param list_type: (optional) the type of the values in the list
    :param error_message: (optional) the message in case the value type mismatch
    :param repeat: (optional) if the list can contain repeated values
    :return: the list entered by the user
    """
    while True:
        items = string_input(text=text, empty=empty, clear=clear).split(sep=sep)
        if clear:
            items = [item.strip() for item in items]
        items = list(filter(None, items))  # Remove the empty values
        if not repeat:
            items = list(dict.fromkeys(items))  # Remove the repeated values
        try:
            return [list_type(item) for item in items]  # Return the list with the items in the right type
        except ValueError:
            print(error_message)


def path_input(text, not_path_error: str = 'Please, enter a valid path!', empty: bool = False, clear: bool = False,
               invalid_paths: list = None) -> str:
    """
    Gets a valid path from the user

    :param text: the text for the user
    :param not_path_error: (optional) the text printed if the string is not a path
    :param empty: (optional) if the string could be empty
    :param clear: (optional) if the extra whitespaces can be removed
    :param invalid_paths: (optional) a list with paths that will not be accepted
    :return: the valid path
    """
    while True:
        path = string_input(text=text, empty=empty, clear=clear)
        if not (os.path.isdir(path) or os.path.isfile(path)):
            if path not in invalid_paths:
                return path
        else:
            print(not_path_error)


def _clear_text(text: str) -> str:
    """
    Removes extra whitespaces

    :param text: the text to be cleared
    :return: the cleared text
    """
    return " ".join(text.split())


def _is_empty(text: str, white_spaces: bool = False) -> bool:
    """
    Verifies if the string is empty

    :param text: the string to be evaluated
    :param white_spaces: (optional) if the string can contain extra whitespaces
    :return: True if it is empty else False
    """
    if not white_spaces:
        text = " ".join(text.split())  # Remove whitespaces
    if text is None or len(text) < 1:
        return True
    return False
