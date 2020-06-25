def clear_text(text: str) -> str:
    """
    Removes extra whitespaces

    :param text: the text to be cleared
    :return: the cleared text
    """
    return " ".join(text.split())
