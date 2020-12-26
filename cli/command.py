class CommandSpec:

    def __init__(self, name: str, aliases: list[str], description: str, params: list, func):
        self.name = name
        self.aliases = aliases
        self.description = description
        self.params = params
        self.func = func


commands = dict[str, CommandSpec]()

# aliases have different display on help command
aliases = dict[str, CommandSpec]()


def command(
        names: list[str],
        description: str,
        arguments: list = None
):

    if len(names) < 1:
        raise SyntaxError('Expected 1 name or more!')

    if arguments is None:
        arguments = []

    command_aliases = names[1:]

    def decorator(func):

        spec = CommandSpec(names[0], command_aliases, description, arguments, func)
        commands[names[0]] = spec

        for alias in command_aliases:
            aliases[alias] = spec

        return func

    return decorator
