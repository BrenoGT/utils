from utils.misc import clear_text


def is_empty(text: str, white_spaces: bool = False) -> bool:
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


def is_extension(ext: str) -> bool:
    """
    Verifies if it is an extension

    :param ext: the extension
    :return: True if it is else False
    """
    if not (ext[0] == '.' and ext[1:].isalnum()):
        return False
    else:
        return True


def confirm(*texts: str, options: dict = {'Confirm': True, 'Cancel': False}, end: str = '\n') -> bool:
    """
    Confirms some choice

    :param texts: the texts to be printed
    :param options: (optional) options on question
    :param end: (optional) the EOL (End Of Line) string
    :return: True if confirmation else False
    """
    for text in texts:
        print(text, end=end)
    options_list = [item for item in options.keys()]
    for index, dict_option in enumerate(options_list):
        print(f'{index + 1}. {dict_option}')
    try:
        option = int(clear_text(input('Option: '))) - 1
    except ValueError:
        print('Please enter a valid integer!\n')
    else:
        try:
            return options[options_list[option]]
        except KeyError:
            print('Invalid option! Choose a valid one!')
