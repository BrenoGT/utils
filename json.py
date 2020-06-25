import json


def read_json(file_path: str, encoding: str = 'utf8') -> json:
    """
    Reads a JSON file

    :param file_path: the path os the file
    :param encoding: (optional) the encoding used in the reading
    :return: the JSON data
    """
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
        file.close()
    return data


def save_json(file_path: str, data: (list, dict), encoding: str = 'utf8', indent: int = 2) -> None:
    """
    Saves data into a JSON file

    :param file_path: the path os the file
    :param data: the data to be saved
    :param encoding: (optional) the encoding used to write the data
    :param indent: (optional) the indentation of the JSON file
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=indent)
        file.close()
