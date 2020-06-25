from utils.inputs import int_input
from utils.validations import is_empty


def show_menu_head(title: str, length: int, up_down_char: str = '*', sides: str = '*') -> None:
    """
    Prints a formatted menu head

    :param title: the menu title
    :param length: (optional) the length of the menu
    :param up_down_char: (optional) the character used to format the layout on top and bottom
    :param sides: (optional) the character used to format the layout on the sides
    """
    if length is None or len(title) > length:
        length = len(title) + 10
    print_line(up_down_char, length)
    print(f'{sides}{title.upper():^{length - 2}}{sides}')
    print_line(up_down_char, length)


def show_menu(title: str, options: list, length: int = None, leave_value: int = None) -> (str, None):
    """
    Prints the menu

    :param title: the menu title
    :param options: the menu options
    :param length: the menu length
    :param leave_value: (optional) value to leave the menu
    :return: the option chosen by the user
    """
    if not is_empty(title):
        show_menu_head(title, length)
    for index, item in enumerate(options):
        print(f'{index + 1}. {item}')
    option = int_input(text='Option: ', min_value=1, max_value=len(options), leave_value=leave_value)
    if option == leave_value:
        return None
    return options[option - 1]


def print_line(string: str, size: int) -> None:
    """
    Prints a formatted line

    :param string: the string to be repeated
    :param size: the time the string will be repeated
    """
    print(f'{string * size}')


def list_items(title: str, items: list, length: int = None) -> None:
    """
    Lists the items

    :param title: the menu title
    :param items: the items
    :param length: the menu length
    """
    if length is None:
        length = len(title) + 10
    elif length < len(title):
        length = len(title)

    if not is_empty(title):
        show_menu_head(title, length)
    for index, item in enumerate(items):
        print(f'{index + 1}. {item}')
