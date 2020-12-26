"""
Dictionary of ANSI escape color
codes by its code. Used by the
colorize function
"""
COLORS = {
    '0': '\u001b[30;1m',
    'a': '\u001b[32;1m',
    'b': '\u001b[34;1m',
    'c': '\u001b[31;1m',
    'd': '\u001b[35;1m',
    'e': '\u001b[33;1m',
    'f': '\u001b[37;1m',
    'r': '\u001b[0m'
}


def prompt(message: str = ''):
    """
    Awaits for the user to introduce something
    adding as prompt a pretty prefix
    :return: The introduced value
    """
    if message != '':
        print(message)
    return input(colorize('$a$ >>  '))


def log(message: str) -> None:
    """
    Colorizes and logs the given message
    to the console out
    :param message: The displayed message
    """
    print(colorize(message + '$r'))


def log_separator() -> None:
    log('$c' + '-' * 70)


def colorize(text: str) -> str:
    """
    Replaces color codes in a format like '$<code>'
    with ANSI escape color codes.
    for example '$0' for black, '$a' for green, etc.
    :param text: The text that will be translated
    :return: The translated text
    """
    value = []
    skip_next = False
    for i in range(len(text) - 1):
        char = text[i]

        if skip_next:
            skip_next = False
            continue

        # Next char is escaped
        if char == '\\':
            skip_next = True
            value.append(text[i + 1])
            continue

        # So next char will be the color
        elif char == '$':
            skip_next = True
            color_code = text[i + 1]
            if color_code in COLORS:
                value.append(COLORS[color_code])
            else:
                value.append(char)
                value.append(color_code)
        else:
            value.append(char)

    value = ''.join(value)
    if not skip_next:
        value += value[-1]
    return value
