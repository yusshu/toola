from cli.command import *
from cli.log import log
from cli.transform.transforming import *


class DispatchError(RuntimeError):

    def __init__(self, message: str, spec: CommandSpec):
        self.spec = spec
        self.message = message
        RuntimeError.__init__(self, message)


def parse(args: list[str], bounds: str):
    types = bounds.split('|')
    errors = []
    for bound in types:
        bound = bound.strip()
        if bound not in transformers:
            raise TransformError(f'No argument transformer for type {bound} exists')
        try:
            return transformers[bound].transform(args)
        except TransformError as err:
            errors.append(err)
    raise errors.pop()


def dispatch_command(line: str):
    # TODO: Change this by a regex tokenizer
    args: list[str] = line.split(' ')
    name = args[0].lower()
    del args[0]

    if name not in commands and name not in aliases:
        log(f'$c | Error >> $rUnknown command: $f{name}')
        return

    spec: CommandSpec = commands[name] if name in commands else aliases[name]
    arguments = []
    cursor = 0

    for parameter in spec.params:

        if 'type' not in parameter:
            raise DispatchError('Parameter doesnt specify a type!', spec)

        if cursor > len(args):
            if 'default' not in parameter:
                raise DispatchError('Few arguments', spec)
            else:
                arguments.append(parameter['default'])
                continue

        transforming_args = args[cursor:] if ('infinite' in parameter) else args[cursor:cursor + 1]
        try:
            arguments.append(parse(transforming_args, parameter['type']))
            cursor += len(transforming_args)
        except TransformError as err:
            cursor += 1
            raise err
        cursor += 1

    if cursor < len(args):
        raise DispatchError('Many arguments', spec)

    pass_args_fmt = []
    for i in range(len(arguments)):
        pass_args_fmt.append(f'arguments[{i}]')

    eval(f'spec.func({", ".join(pass_args_fmt)})')
