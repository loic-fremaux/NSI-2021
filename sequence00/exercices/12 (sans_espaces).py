def sans_espaces(string: str):
    """
    Remove blank spaces of a string
    :param string: the string
    :return: the string without blank spaces
    """
    result = ""
    for c in string:
        if c != ' ':
            result += c
    return result


print(sans_espaces("vive la nsi"))
